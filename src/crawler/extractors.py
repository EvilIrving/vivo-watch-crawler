"""
内容提取器模块

负责从页面中提取导航结构、正文内容和代码示例
"""

import logging
import re
from typing import Optional, List, Dict
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class NavigationExtractor:
    """导航提取器 - 从侧边栏提取文档结构"""
    
    def __init__(self, base_url: str):
        """
        初始化导航提取器
        
        Args:
            base_url: 网站基础 URL
        """
        self.base_url = base_url
        
    def extract_sidebar_nav(self, html: str) -> Dict:
        """
        提取侧边栏导航结构
        
        Args:
            html: 页面 HTML 内容
            
        Returns:
            导航结构字典
        """
        try:
            soup = BeautifulSoup(html, 'lxml')
            links = []
            
            # 尝试多个侧边栏选择器
            sidebar_selectors = [
                '#sidebar',
                '.toc-entries',
                '.sidebar',
                '[class*="sidebar"]',
                'aside',
                '.menu',
                '.navigation',
                '[class*="nav"]',
                '.doc-nav'
            ]
            
            sidebar = None
            for selector in sidebar_selectors:
                element = soup.select_one(selector)
                if element and len(element.find_all('a', href=True)) > 5:
                    sidebar = element
                    logger.info(f"找到侧边栏: {selector}")
                    break
            
            if sidebar:
                # 提取侧边栏中的所有链接
                for link in sidebar.find_all('a', href=True):
                    href = link.get('href')
                    text = link.get_text(strip=True)
                    
                    if not href or not text:
                        continue
                    
                    # 清理 URL
                    if '?' in href:
                        href = href.split('?')[0]
                    
                    # 转换为绝对 URL
                    absolute_url = urljoin(self.base_url, href)
                    normalized_url = self._normalize_url(absolute_url)
                    
                    # 过滤无效链接
                    if 'developers.vivo.com' in normalized_url:
                        if not any(l['url'] == normalized_url for l in links):
                            links.append({
                                'text': text,
                                'url': normalized_url
                            })
            else:
                # 备用方案:提取所有文档链接
                logger.warning("未找到侧边栏,使用备用方案")
                links = self._extract_all_doc_links(soup)
            
            logger.info(f"提取到 {len(links)} 个导航链接")
            return {"links": links}
            
        except Exception as e:
            logger.error(f"提取侧边栏导航失败: {str(e)}")
            return {"links": []}
    
    def _extract_all_doc_links(self, soup: BeautifulSoup) -> List[Dict]:
        """备用方案:直接从页面提取所有文档链接"""
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            text = link.get_text(strip=True)
            
            # 匹配文档链接
            if href and text and (
                '/doc/common/reference/' in href or 
                '/doc/common/js/' in href or 
                '/doc/common/component/' in href or
                href.startswith('/reference/') or 
                href.startswith('/js/') or 
                href.startswith('/component/')
            ):
                # 清理 URL
                if '?' in href:
                    href = href.split('?')[0]
                
                absolute_url = urljoin(self.base_url, href)
                normalized_url = self._normalize_url(absolute_url)
                
                if 'developers.vivo.com' in normalized_url:
                    if not any(l['url'] == normalized_url for l in links):
                        links.append({
                            'text': text,
                            'url': normalized_url
                        })
        
        logger.info(f"备用方案提取到 {len(links)} 个链接")
        return links
            
    def _normalize_url(self, url: str) -> str:
        """
        规范化 URL
        
        Args:
            url: 原始 URL
            
        Returns:
            规范化后的 URL
        """
        # 去除锚点
        if '#' in url:
            url = url.split('#')[0]
        # 去除末尾斜杠
        url = url.rstrip('/')
        return url


class ContentExtractor:
    """内容提取器 - 从页面提取正文和代码示例"""
    
    def __init__(self):
        """初始化内容提取器"""
        pass
        
    def extract_page_content(self, html: str, url: str = "") -> Dict:
        """
        提取页面内容
        
        Args:
            html: 页面 HTML
            url: 页面 URL (可选,用于日志)
            
        Returns:
            内容字典
        """
        try:
            soup = BeautifulSoup(html, 'lxml')
            
            # 提取页面标题
            title = self._extract_title(soup)
            
            # 提取面包屑导航
            breadcrumb = self._extract_breadcrumb(soup)
            
            # 提取主内容区域
            main_content = self._extract_main_content(soup)
            
            # 提取代码示例
            code_examples = self._extract_code_examples(soup)
            
            # 提取纯文本内容
            text_content = self._extract_text_content(main_content) if main_content else ""
            
            return {
                'title': title,
                'breadcrumb': breadcrumb,
                'content_html': str(main_content) if main_content else "",
                'content_text': text_content,
                'code_examples': code_examples,
                'has_content': bool(main_content and text_content)
            }
            
        except Exception as e:
            logger.error(f"提取页面内容失败: {str(e)}")
            return {
                'title': '',
                'breadcrumb': [],
                'content_html': '',
                'content_text': '',
                'code_examples': [],
                'has_content': False
            }
            
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """提取页面标题"""
        # 从 HTML 中提取 h1 标题
        h1 = soup.find('h1')
        if h1:
            return h1.get_text(strip=True)
        
        # 从 title 标签提取
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            if title and title != 'vivo开放平台 开发者':
                return title
            
        # 从 meta 标签提取
        meta_title = soup.find('meta', property='og:title')
        if meta_title and meta_title.get('content'):
            return meta_title.get('content')
            
        return ""
        
    def _extract_breadcrumb(self, soup: BeautifulSoup) -> List[str]:
        """提取面包屑导航"""
        breadcrumb = []
        
        # 尝试查找面包屑容器
        breadcrumb_selectors = [
            '.breadcrumb',
            '[class*="breadcrumb"]',
            'nav[aria-label*="breadcrumb"]'
        ]
        
        for selector in breadcrumb_selectors:
            container = soup.select_one(selector)
            if container:
                for item in container.find_all('a'):
                    text = item.get_text(strip=True)
                    if text:
                        breadcrumb.append(text)
                break
                
        return breadcrumb
        
    def _extract_main_content(self, soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """提取主内容区域"""
        # 尝试多个可能的主内容选择器
        main_selectors = [
            'div.html-content',
            'main',
            '.main-content',
            '.doc-content',
            '.content',
            'article',
            '[class*="main"]',
            '[class*="content"]',
            '#content'
        ]
        
        for selector in main_selectors:
            main = soup.select_one(selector)
            if main:
                # 移除侧边栏、导航栏等无关内容
                for unwanted in main.select('.sidebar, .navigation, header, footer, nav'):
                    unwanted.decompose()
                return main
                
        # 如果找不到明确的主内容区域,尝试找到包含最多文本的 div
        all_divs = soup.find_all('div')
        if all_divs:
            # 按文本长度排序
            sorted_divs = sorted(all_divs, key=lambda d: len(d.get_text(strip=True)), reverse=True)
            if sorted_divs and len(sorted_divs[0].get_text(strip=True)) > 100:
                return sorted_divs[0]
                
        return None
        
    def _extract_code_examples(self, soup: BeautifulSoup) -> List[Dict]:
        """提取代码示例"""
        code_examples = []
        
        # 查找所有代码块
        code_blocks = soup.find_all(['pre', 'code'])
        
        for i, block in enumerate(code_blocks):
            # 跳过行内代码
            if block.name == 'code' and block.parent.name != 'pre':
                continue
                
            # 获取代码内容
            if block.name == 'pre':
                code_tag = block.find('code')
                code_text = code_tag.get_text() if code_tag else block.get_text()
            else:
                code_text = block.get_text()
                
            # 提取语言标记
            language = self._detect_code_language(block)
            
            # 提取代码说明(前面的文本或注释)
            description = self._extract_code_description(block)
            
            if code_text.strip():
                code_examples.append({
                    'code': code_text.strip(),
                    'language': language,
                    'description': description,
                    'index': i
                })
                
        logger.debug(f"提取到 {len(code_examples)} 个代码示例")
        return code_examples
        
    def _detect_code_language(self, element) -> str:
        """检测代码语言"""
        # 从 class 属性检测
        class_attr = element.get('class', [])
        if isinstance(class_attr, list):
            for cls in class_attr:
                # 常见的语言标记格式
                if cls.startswith('language-'):
                    return cls.replace('language-', '')
                if cls.startswith('lang-'):
                    return cls.replace('lang-', '')
                # 直接语言名称
                if cls in ['javascript', 'js', 'python', 'java', 'css', 'html', 'json', 'xml']:
                    return cls
                    
        # 从 data-lang 属性检测
        data_lang = element.get('data-lang')
        if data_lang:
            return data_lang
            
        return 'text'
        
    def _extract_code_description(self, element) -> str:
        """提取代码说明"""
        # 查找前面的兄弟元素中的文本
        prev = element.find_previous_sibling()
        if prev and prev.name in ['p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            text = prev.get_text(strip=True)
            if len(text) < 200:  # 只保留较短的说明
                return text
        return ""
        
    def _extract_text_content(self, element) -> str:
        """提取纯文本内容"""
        if not element:
            return ""
            
        # 移除 script 和 style 标签
        for tag in element.find_all(['script', 'style']):
            tag.decompose()
            
        # 获取文本内容
        text = element.get_text(separator='\n', strip=True)
        
        # 清理多余的空白
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        
        return text
