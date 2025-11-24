"""
BlueOS Studio 爬虫调度器
"""

import logging
from typing import Set
import json
from pathlib import Path
from bs4 import BeautifulSoup

from .blueos_studio_crawler import BlueOSStudioCrawler
from .storage import DataStorage

logger = logging.getLogger(__name__)


class BlueOSScheduler:
    """BlueOS Studio 爬虫调度器"""
    
    def __init__(self, config: dict):
        """初始化调度器"""
        self.config = config
        self.crawler = BlueOSStudioCrawler(config)
        self.storage = DataStorage(config.get('data_dir', 'data'))
        
        # 统计信息
        self.stats = {
            'total_urls': 0,
            'success_count': 0,
            'failed_count': 0,
            'skipped_count': 0
        }
        
        self.visited_paths: Set[str] = set()
    
    def start(self):
        """启动爬虫"""
        logger.info("=" * 60)
        logger.info("开始爬取 BlueOS Studio 文档")
        logger.info("=" * 60)
        
        try:
            # 加载已爬取的路径
            self.visited_paths = self.storage.load_crawled_urls()
            
            # 发现所有页面
            logger.info("\n阶段一: 发现所有页面")
            logger.info("=" * 60)
            
            paths = self.crawler.discover_pages_from_sidebar()
            logger.info(f"发现 {len(paths)} 个页面\n")
            
            self.stats['total_urls'] = len(paths)
            
            # 爬取所有页面
            logger.info("\n阶段二: 爬取所有页面")
            logger.info("=" * 60)
            
            for i, path in enumerate(paths, 1):
                logger.info(f"\n[{i}/{len(paths)}] 处理: {path}")
                
                # 检查是否已爬取
                if path in self.visited_paths:
                    logger.info("  ⊙ 已爬取，跳过")
                    self.stats['skipped_count'] += 1
                    continue
                
                # 爬取页面
                success = self._crawl_page(path)
                
                if success:
                    self.visited_paths.add(path)
                    self.stats['success_count'] += 1
                else:
                    self.stats['failed_count'] += 1
                
                # 延迟
                if i < len(paths):
                    self.crawler.delay()
                
                # 打印进度
                if i % 10 == 0:
                    self._print_progress()
            
            # 保存统计信息
            self.storage.save_statistics(self.stats)
            
            # 打印总结
            self._print_summary()
            
        finally:
            self.crawler.close()
    
    def _crawl_page(self, path: str) -> bool:
        """爬取单个页面"""
        try:
            # 获取页面数据
            page_data = self.crawler.get_page_data(path)
            
            if not page_data:
                logger.warning("  ✗ 未获取到数据")
                return False
            
            # 从 HTML 提取内容
            content = self._extract_content(page_data)
            
            if not content.get('has_content'):
                logger.warning("  ✗ 未提取到有效内容")
                return False
            
            # 确定分类
            category = self._categorize_path(path)
            
            # 构造完整 URL
            full_url = f"https://studio.blueos.com.cn{path}"
            
            # 保存数据
            self.storage.save_page_data(full_url, category, content, 'success')
            
            logger.info(f"  ✓ 成功: {content.get('title', 'Untitled')}")
            return True
            
        except Exception as e:
            logger.error(f"  ✗ 失败: {str(e)}")
            return False
    
    def _extract_content(self, page_data: dict) -> dict:
        """从页面数据中提取内容"""
        html = page_data.get('html', '')
        frontmatter = page_data.get('frontmatter', {})
        
        if not html:
            return {'has_content': False}
        
        # HTML 已经是字符串，直接解析
        soup = BeautifulSoup(html, 'html.parser')
        
        # 提取标题
        title = frontmatter.get('title', '')
        if not title:
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text(strip=True)
        
        # 提取面包屑导航
        breadcrumb = []
        breadcrumb_elem = soup.select_one('.breadcrumb') or soup.select_one('.breadcrumbs')
        if breadcrumb_elem:
            breadcrumb = [item.get_text(strip=True) for item in breadcrumb_elem.find_all(['a', 'span'])]
        
        # 提取纯文本
        text_content = soup.get_text(separator='\n', strip=True)
        
        # 提取代码示例
        code_examples = []
        for i, pre in enumerate(soup.find_all('pre')):
            code_tag = pre.find('code')
            if code_tag:
                code_text = code_tag.get_text()
                # 提取语言
                language = 'text'
                class_attr = code_tag.get('class', [])
                for cls in class_attr:
                    if cls.startswith('language-'):
                        language = cls.replace('language-', '')
                        break
                
                code_examples.append({
                    'code': code_text.strip(),
                    'language': language,
                    'index': i
                })
        
        return {
            'title': title,
            'breadcrumb': breadcrumb,
            'content_html': html,
            'content_text': text_content,
            'code_examples': code_examples,
            'frontmatter': frontmatter,
            'has_content': bool(html and text_content)
        }
    
    def _categorize_path(self, path: str) -> str:
        """根据路径判断分类"""
        if '/explore/' in path:
            return 'blueos-explore'
        elif '/write/' in path:
            return 'blueos-write'
        elif '/deploy/' in path:
            return 'blueos-deploy'
        else:
            return 'blueos-other'
    
    def _print_progress(self):
        """打印进度"""
        total_processed = self.stats['success_count'] + self.stats['failed_count'] + self.stats['skipped_count']
        total = self.stats['total_urls']
        percentage = (total_processed / total * 100) if total > 0 else 0
        
        logger.info(f"\n进度: {total_processed}/{total} ({percentage:.1f}%) "
                   f"| 成功: {self.stats['success_count']} "
                   f"| 失败: {self.stats['failed_count']} "
                   f"| 跳过: {self.stats['skipped_count']}\n")
    
    def _print_summary(self):
        """打印总结"""
        logger.info("\n" + "=" * 60)
        logger.info("爬取完成")
        logger.info("=" * 60)
        logger.info(f"总页面数: {self.stats['total_urls']}")
        logger.info(f"成功: {self.stats['success_count']}")
        logger.info(f"失败: {self.stats['failed_count']}")
        logger.info(f"跳过: {self.stats['skipped_count']}")
        
        if self.stats['total_urls'] > 0:
            success_rate = (self.stats['success_count'] + self.stats['skipped_count']) / self.stats['total_urls'] * 100
            logger.info(f"成功率: {success_rate:.1f}%")
        
        logger.info("=" * 60)


# 修复导入问题，添加BeautifulSoup导入