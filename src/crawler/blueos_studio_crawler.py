"""
BlueOS Studio 网站爬虫
处理 https://studio.blueos.com.cn/ 站点的内容
"""

import logging
import time
import random
from typing import Optional, Dict, List
from urllib.parse import urljoin, urlparse
import requests∏
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class BlueOSStudioCrawler:
    """BlueOS Studio 网站爬虫"""
    
    def __init__(self, config: dict):
        """初始化爬虫"""
        self.config = config
        self.base_url = "https://studio.blueos.com.cn"
        self.timeout = config.get('timeout', 30)
        self.delay_range = config.get('delay_range', [0.5, 1.5])
        
        # 创建 session
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': config.get('user_agent', 'Mozilla/5.0'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://studio.blueos.com.cn/'
        })
        
    def get_page_data(self, path: str) -> Optional[Dict]:
        """
        获取页面数据
        
        Args:
            path: 页面路径，如 '/explore/intro'
            
        Returns:
            页面数据字典
        """
        try:
            # 构造完整 URL
            clean_path = path.strip('/')
            page_url = f"{self.base_url}/{clean_path}"
            
            logger.info(f"请求页面: {page_url}")
            
            response = self.session.get(page_url, timeout=self.timeout)
            response.raise_for_status()
            
            # 解析页面内容
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取标题
            title = ''
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text(strip=True)
            
            # 提取主要内容区域
            # 根据实际页面结构调整选择器
            content_div = soup.select_one('.markdown-body') or \
                         soup.select_one('.content') or \
                         soup.select_one('main') or \
                         soup.select_one('.container') or \
                         soup
            
            html_content = str(content_div) if content_div else response.text
            
            return {
                'html': html_content,
                'frontmatter': {'title': title},
                'path': path,
                'source_url': page_url
            }
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.warning(f"页面不存在: {page_url}")
            else:
                logger.error(f"HTTP 错误: {page_url}, 状态码: {e.response.status_code}")
            return None
        except Exception as e:
            logger.error(f"获取页面失败: {page_url}, 错误: {str(e)}")
            return None
    
    def discover_pages_from_sidebar(self) -> List[str]:
        """
        从侧边栏发现所有页面路径
        
        Returns:
            页面路径列表
        """
        try:
            logger.info("从侧边栏自动发现所有文档链接...")
            paths = self._extract_sidebar_links()
            if paths:
                logger.info(f"从侧边栏发现 {len(paths)} 个页面")
                return sorted(list(set(paths)))  # 去重并排序
        except Exception as e:
            logger.warning(f"从侧边栏发现页面失败: {str(e)}")
        
        # 如果侧边栏发现失败，使用预定义路径
        logger.info("使用预定义路径模式")
        return self._get_predefined_paths()
    
    def _extract_sidebar_links(self) -> List[str]:
        """从侧边栏提取链接"""
        all_paths = set()
        
        # 先访问主页或指定页面来获取侧边栏
        sample_urls = [
            f"{self.base_url}/explore/intro",
            f"{self.base_url}/write/create-component",
        ]
        
        for sample_url in sample_urls:
            try:
                logger.debug(f"从 {sample_url} 提取侧边栏链接...")
                response = self.session.get(sample_url, timeout=self.timeout)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 查找侧边栏中的所有链接
                # 根据实际页面结构调整选择器
                sidebar_selectors = [
                    '.sidebar a[href]',
                    '.side-nav a[href]', 
                    '.nav-menu a[href]',
                    'aside a[href]',
                    '[class*="sidebar"] a[href]'
                ]
                
                links_found = False
                for selector in sidebar_selectors:
                    links = soup.select(selector)
                    if links:
                        logger.debug(f"使用选择器 '{selector}' 找到 {len(links)} 个链接")
                        for link in links:
                            href = link.get('href', '')
                            if href:
                                # 处理相对链接和绝对链接
                                if href.startswith('http'):
                                    # 检查是否属于同一域名
                                    parsed_href = urlparse(href)
                                    if parsed_href.netloc == 'studio.blueos.com.cn':
                                        path = parsed_href.path
                                    else:
                                        continue
                                elif href.startswith('/'):
                                    path = href
                                else:
                                    # 相对路径
                                    path = '/' + href
                                
                                # 只保留有效的文档路径
                                if path and (path.startswith('/explore/') or path.startswith('/write/')):
                                    all_paths.add(path)
                                    links_found = True
                        
                        if links_found:
                            break  # 找到链接就跳出，尝试下一个选择器
                
            except Exception as e:
                logger.warning(f"从 {sample_url} 提取链接失败: {str(e)}")
                continue
        
        if not all_paths:
            raise Exception("未能从侧边栏提取到链接")
        
        return list(all_paths)
    
    def _get_predefined_paths(self) -> List[str]:
        """获取预定义的路径列表"""
        # 根据目标网站的实际结构预定义一些路径
        paths = [
            '/explore/intro',
            '/explore/getting-started',
            '/explore/project-structure',
            '/write/create-component',
            '/write/create-page',
            '/write/create-widget',
            '/write/navigation',
            '/deploy/build',
            '/deploy/publish',
        ]
        
        return paths
    
    def delay(self):
        """添加随机延迟"""
        delay = random.uniform(*self.delay_range)
        time.sleep(delay)
    
    def close(self):
        """关闭连接"""
        self.session.close()


def test_blueos_studio_crawler():
    """测试 BlueOS Studio 爬虫"""
    logging.basicConfig(level=logging.INFO)
    
    config = {
        'timeout': 30,
        'delay_range': [0.5, 1],
        'user_agent': 'Mozilla/5.0'
    }
    
    crawler = BlueOSStudioCrawler(config)
    
    try:
        # 测试发现页面
        print(f"\n{'='*60}")
        print("测试: 自动发现所有文档页面")
        print('='*60)
        paths = crawler.discover_pages_from_sidebar()
        print(f"发现 {len(paths)} 个页面")
        for path in paths[:10]:  # 只显示前10个
            print(f"  - {path}")
        
        # 测试获取页面
        print(f"\n{'='*60}")
        print("测试: 获取示例页面")
        print('='*60)
        
        test_paths = ['/explore/intro', '/write/create-component'] if len(paths) == 0 else paths[:2]
        for i, path in enumerate(test_paths, 1):
            print(f"\n[{i}/{len(test_paths)}] 测试: {path}")
            data = crawler.get_page_data(path)
            if data:
                title = data.get('frontmatter', {}).get('title', 'No title')
                html_len = len(data.get('html', ''))
                print(f"  ✓ 成功 - 标题: {title}")
                print(f"  HTML 长度: {html_len} 字符")
            else:
                print(f"  ✗ 失败")
            
            if i < len(test_paths):
                crawler.delay()
        
    finally:
        crawler.close()


if __name__ == "__main__":
    test_blueos_studio_crawler()