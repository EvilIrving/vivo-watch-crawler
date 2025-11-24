"""
爬虫调度器

负责管理爬取队列、URL 去重和整体爬取流程
"""

import logging
import random
import time
from collections import deque
from typing import Set, Dict

from .browser_engine import HTTPEngine
from .extractors import NavigationExtractor, ContentExtractor
from .storage import DataStorage

logger = logging.getLogger(__name__)


class CrawlerScheduler:
    """爬虫调度器"""
    
    def __init__(self, config: dict):
        """
        初始化调度器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.base_url = config.get('base_url', '')
        self.entry_urls = config.get('entry_urls', [])
        self.max_workers = config.get('max_workers', 3)
        self.retry_times = config.get('retry_times', 3)
        self.delay_range = config.get('delay_range', [1, 3])
        
        # URL 队列和去重集合
        self.url_queue: deque = deque()
        self.visited_urls: Set[str] = set()
        self.failed_urls: Dict[str, int] = {}  # URL -> 失败次数
        
        # 统计信息
        self.stats = {
            'total_urls': 0,
            'success_count': 0,
            'failed_count': 0,
            'skipped_count': 0
        }
        
        # 初始化组件
        self.http_engine = HTTPEngine(
            user_agent=config.get('user_agent'),
            timeout=config.get('timeout', 30)
        )
        self.nav_extractor = NavigationExtractor(self.base_url)
        self.content_extractor = ContentExtractor()
        self.storage = DataStorage(config.get('data_dir', 'data'))
        
        # 导航结构
        self.all_links = []
        
    def start(self):
        """启动爬虫"""
        logger.info("=" * 60)
        logger.info("开始爬取 vivo 手表文档")
        logger.info("=" * 60)
        
        try:
            # 加载已爬取的 URL(断点续爬)
            self.visited_urls = self.storage.load_crawled_urls()
            
            # 添加入口 URL 到队列
            for url in self.entry_urls:
                self.add_url(url)
                
            # 第一阶段:从入口页面提取所有导航链接
            self._extract_all_navigation_links()
            
            # 第二阶段:爬取所有页面
            self._crawl_all_pages()
            
            # 保存统计信息
            self.storage.save_statistics(self.stats)
            
            # 打印总结
            self._print_summary()
            
        finally:
            self.http_engine.close()
            
    def _extract_all_navigation_links(self):
        """从入口页面提取所有导航链接"""
        logger.info("\n" + "=" * 60)
        logger.info("阶段一:提取导航结构")
        logger.info("=" * 60)
        
        all_nav_links = []
        
        for entry_url in self.entry_urls:
            try:
                logger.info(f"\n处理入口: {entry_url}")
                html = self.http_engine.get_page(entry_url)
                
                if not html:
                    logger.error(f"无法获取页面内容: {entry_url}")
                    continue
                
                # 提取侧边栏导航
                nav_data = self.nav_extractor.extract_sidebar_nav(html)
                links = nav_data.get('links', [])
                
                all_nav_links.extend(links)
                logger.info(f"从入口提取到 {len(links)} 个链接")
                
                # 添加延迟
                self._random_delay()
                
            except Exception as e:
                logger.error(f"提取导航失败: {entry_url}, 错误: {str(e)}")
                
        # 去重并添加到队列
        unique_links = {}
        for link in all_nav_links:
            url = link['url']
            if url not in unique_links:
                unique_links[url] = link
                
        self.all_links = list(unique_links.values())
        logger.info(f"\n总共发现 {len(self.all_links)} 个唯一链接")
        
        # 保存导航结构
        self.storage.save_navigation_structure({
            'total_links': len(self.all_links),
            'links': self.all_links
        })
        
        # 添加所有链接到队列
        for link in self.all_links:
            self.add_url(link['url'])
            
        self.stats['total_urls'] = len(self.url_queue)
        
    def _crawl_all_pages(self):
        """爬取所有页面"""
        logger.info("\n" + "=" * 60)
        logger.info("阶段二:爬取所有页面")
        logger.info("=" * 60)
        logger.info(f"待爬取页面数: {len(self.url_queue)}\n")
        
        # 顺序爬取所有页面
        while self.url_queue:
            url = self.url_queue.popleft()
            
            # 检查是否已访问
            if url in self.visited_urls:
                self.stats['skipped_count'] += 1
                continue
                
            # 爬取页面
            success = self._crawl_single_page(url)
            
            if success:
                self.visited_urls.add(url)
                self.stats['success_count'] += 1
            else:
                # 重试逻辑
                retry_count = self.failed_urls.get(url, 0)
                if retry_count < self.retry_times:
                    self.failed_urls[url] = retry_count + 1
                    self.url_queue.append(url)  # 重新加入队列
                    logger.warning(f"将重试 ({retry_count + 1}/{self.retry_times}): {url}")
                else:
                    self.stats['failed_count'] += 1
                    logger.error(f"达到最大重试次数,放弃: {url}")
                    
            # 添加延迟
            self._random_delay()
            
            # 打印进度
            if (self.stats['success_count'] + self.stats['failed_count']) % 10 == 0:
                self._print_progress()
                
    def _crawl_single_page(self, url: str) -> bool:
        """
        爬取单个页面
        
        Args:
            url: 页面 URL
            
        Returns:
            是否成功
        """
        try:
            logger.info(f"爬取: {url}")
            self.storage.log_crawl_event('start', url)
            
            # 获取页面
            html = self.http_engine.get_page(url)
            
            if not html:
                logger.warning(f"无法获取页面内容: {url}")
                self.storage.log_crawl_event('error', url, {'reason': 'no_html'})
                return False
            
            # 提取内容
            content = self.content_extractor.extract_page_content(html, url)
            
            # 检查是否提取到有效内容
            if not content.get('has_content'):
                logger.warning(f"未提取到有效内容: {url}")
                self.storage.log_crawl_event('error', url, {'reason': 'no_content'})
                return False
                
            # 确定分类
            category = self._categorize_url(url)
            
            # 保存数据
            self.storage.save_page_data(url, category, content, 'success')
            self.storage.log_crawl_event('success', url, {
                'title': content.get('title'),
                'code_examples_count': len(content.get('code_examples', []))
            })
            
            logger.info(f"✓ 成功: {content.get('title', 'Untitled')}")
            return True
            
        except Exception as e:
            logger.error(f"✗ 失败: {url}, 错误: {str(e)}")
            self.storage.log_crawl_event('error', url, {'error': str(e)})
            return False
            
    def add_url(self, url: str):
        """添加 URL 到队列"""
        if url not in self.visited_urls and url not in [u for u in self.url_queue]:
            # 只添加符合条件的 URL
            if self.base_url in url:
                self.url_queue.append(url)
                
    def _categorize_url(self, url: str) -> str:
        """根据 URL 判断分类"""
        if '/reference/' in url or '/quickstart/' in url:
            return 'tutorial'
        elif '/js/' in url:
            return 'js-api'
        elif '/component/' in url:
            return 'ui-component'
        else:
            return 'other'
            
    def _random_delay(self):
        """添加随机延迟"""
        delay = random.uniform(*self.delay_range)
        time.sleep(delay)
        
    def _print_progress(self):
        """打印爬取进度"""
        total_processed = self.stats['success_count'] + self.stats['failed_count']
        total = self.stats['total_urls']
        percentage = (total_processed / total * 100) if total > 0 else 0
        
        logger.info(f"\n进度: {total_processed}/{total} ({percentage:.1f}%) "
                   f"| 成功: {self.stats['success_count']} "
                   f"| 失败: {self.stats['failed_count']}\n")
        
    def _print_summary(self):
        """打印爬取总结"""
        logger.info("\n" + "=" * 60)
        logger.info("爬取完成")
        logger.info("=" * 60)
        logger.info(f"总页面数: {self.stats['total_urls']}")
        logger.info(f"成功: {self.stats['success_count']}")
        logger.info(f"失败: {self.stats['failed_count']}")
        logger.info(f"跳过: {self.stats['skipped_count']}")
        
        if self.stats['total_urls'] > 0:
            success_rate = self.stats['success_count'] / self.stats['total_urls'] * 100
            logger.info(f"成功率: {success_rate:.1f}%")
        
        logger.info("=" * 60)
