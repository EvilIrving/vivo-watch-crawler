"""
API 爬虫 - 通过 HTML API 获取文档数据

vivo 开发者网站文档通过 ?hastopwindow=1 参数获取完整 HTML 页面
"""

import logging
import json
import time
import random
from typing import Optional, Dict, List
from urllib.parse import urlparse, urljoin
import requests

logger = logging.getLogger(__name__)


class APIPageCrawler:
    """基于 API 的页面爬虫"""
    
    def __init__(self, config: dict):
        """初始化爬虫"""
        self.config = config
        self.base_url = "https://developers-watch.vivo.com.cn"
        self.api_base = "https://developers-watch.vivo.com.cn/page-data"
        self.timeout = config.get('timeout', 30)
        self.delay_range = config.get('delay_range', [0.5, 1.5])
        
        # 创建 session
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': config.get('user_agent', 'Mozilla/5.0'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://developers-watch.vivo.com.cn/'
        })
        
    def get_page_data(self, path: str) -> Optional[Dict]:
        """
        获取页面数据
        
        Args:
            path: 页面路径，如 '/api/system/app/'
            
        Returns:
            页面数据字典
        """
        try:
            # 方法1: 直接访问 HTML 页面（带 hastopwindow 参数）
            clean_path = path.strip('/')
            html_url = f"{self.base_url}/{clean_path}?hastopwindow=1"
            
            logger.info(f"请求 HTML: {html_url}")
            
            response = self.session.get(html_url, timeout=self.timeout)
            response.raise_for_status()
            
            # 使用 BeautifulSoup 提取文档内容
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取主内容区域
            content_div = soup.select_one('.html-content')
            if not content_div:
                logger.warning(f"未找到内容区域: {html_url}")
                return None
            
            # 提取 HTML 内容
            html_content = str(content_div)
            
            # 提取标题
            title = ''
            h1 = content_div.select_one('h1')
            if h1:
                title = h1.get_text(strip=True)
            
            return {
                'html': html_content,
                'frontmatter': {'title': title},
                'path': path,
                'source_url': html_url
            }
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.warning(f"页面不存在: {html_url}")
            else:
                logger.error(f"HTTP 错误: {html_url}, 状态码: {e.response.status_code}")
            return None
        except Exception as e:
            logger.error(f"获取页面失败: {html_url}, 错误: {str(e)}")
            return None
    
    def discover_pages_from_sitemap(self) -> List[str]:
        """
        从 sitemap 或其他方式发现所有页面路径
        
        Returns:
            页面路径列表
        """
        # 优先从导航页面提取所有链接
        try:
            logger.info("从导航页面自动发现所有文档链接...")
            paths = self._discover_from_navigation()
            if paths:
                logger.info(f"从导航发现 {len(paths)} 个页面")
                return paths
        except Exception as e:
            logger.warning(f"从导航发现页面失败: {str(e)}")
        
        # 如果导航发现失败，使用预定义路径
        logger.info("使用预定义路径模式")
        return self._get_predefined_paths()
    
    def _discover_from_navigation(self) -> List[str]:
        """从导航页面发现所有文档链接"""
        from bs4 import BeautifulSoup
        
        all_paths = set()
        
        # 从多个页面获取导航链接，以覆盖所有分类
        sample_urls = [
            f"{self.base_url}/api/system/app?hastopwindow=1",  # API 文档
            f"{self.base_url}/reference/quickstart/introduction?hastopwindow=1",  # 教程文档
            f"{self.base_url}/component/common/rule?hastopwindow=1",  # UI 组件文档
        ]
        
        for sample_url in sample_urls:
            try:
                logger.debug(f"从 {sample_url} 提取链接...")
                response = self.session.get(sample_url, timeout=self.timeout)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 提取侧边栏中的所有链接
                links = soup.select('a.nav-links-item[href]')
                
                for link in links:
                    href = link.get('href', '')
                    # 移除参数
                    path = href.split('?')[0]
                    if path and path.startswith('/'):
                        all_paths.add(path)
                        
            except Exception as e:
                logger.warning(f"从 {sample_url} 提取链接失败: {str(e)}")
                continue
        
        if not all_paths:
            raise Exception("未能从任何导航页面提取到链接")
        
        return sorted(all_paths)
    
    def _parse_sitemap(self, xml_content: str) -> List[str]:
        """解析 sitemap XML"""
        from bs4 import BeautifulSoup
        
        paths = []
        soup = BeautifulSoup(xml_content, 'xml')
        
        # 查找所有 URL
        for loc in soup.find_all('loc'):
            url = loc.get_text()
            # 提取路径部分
            parsed = urlparse(url)
            if parsed.path and parsed.path != '/':
                # 过滤掉 sitemap 自身的路径
                if not parsed.path.startswith('/sitemap/'):
                    paths.append(parsed.path)
        
        return paths
    
    def _get_predefined_paths(self) -> List[str]:
        """获取预定义的路径列表 - 基于实际验证的有效路径"""
        paths = []
        
        # 参考文档 - 快速入门
        paths.extend([
            '/reference/quickstart/introduction/',
            '/reference/quickstart/quick-start/',
        ])
        
        # 参考文档 - 小组件开发
        paths.extend([
            '/reference/widget/project-config/',
            '/reference/widget/lite-widget/',
        ])
        
        # JS API - 系统能力
        paths.extend([
            '/api/system/app/',
            '/api/system/device/',
            '/api/system/router/',
            '/api/system/vibrator/',
            '/api/system/brightness/',
            '/api/system/battery/',
            '/api/system/geolocation/',
            '/api/system/sensor/',
        ])
        
        # UI 组件 - 通用规则
        paths.extend([
            '/component/common/rule/',
        ])
        
        # UI 组件 - 基础组件
        paths.extend([
            '/component/basic/text/',
            '/component/basic/image/',
            '/component/basic/progress/',
        ])
        
        # UI 组件 - 容器组件
        paths.extend([
            '/component/container/div/',
            '/component/container/list/',
            '/component/container/list-item/',
            '/component/container/stack/',
            '/component/container/swiper/',
        ])
        
        return paths
    
    def delay(self):
        """添加随机延迟"""
        delay = random.uniform(*self.delay_range)
        time.sleep(delay)
    
    def close(self):
        """关闭连接"""
        self.session.close()


def test_api_crawler():
    """测试 API 爬虫"""
    logging.basicConfig(level=logging.INFO)
    
    config = {
        'timeout': 30,
        'delay_range': [0.5, 1],
        'user_agent': 'Mozilla/5.0'
    }
    
    crawler = APIPageCrawler(config)
    
    try:
        # 测试发现页面
        print(f"\n{'='*60}")
        print("测试: 自动发现所有文档页面")
        print('='*60)
        paths = crawler.discover_pages_from_sitemap()
        print(f"发现 {len(paths)} 个页面")
        
        # 测试获取页面
        print(f"\n{'='*60}")
        print("测试: 获取示例页面")
        print('='*60)
        
        test_paths = paths[:5]
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
    test_api_crawler()
