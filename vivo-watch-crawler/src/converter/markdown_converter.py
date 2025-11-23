"""
Markdown 转换器

将 HTML 内容转换为格式良好的 Markdown 文档
"""

import logging
import re
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

logger = logging.getLogger(__name__)


class MarkdownConverter:
    """Markdown 转换器"""
    
    def __init__(self, output_dir: str = "output/markdown"):
        """
        初始化转换器
        
        Args:
            output_dir: 输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def convert_page(self, record: dict, category: str) -> dict:
        """
        转换单个页面为 Markdown
        
        Args:
            record: 页面记录
            category: 分类
            
        Returns:
            转换结果字典
        """
        try:
            # 提取基本信息
            url = record.get('url', '')
            title = record.get('title', 'Untitled')
            breadcrumb = record.get('breadcrumb', [])
            content_html = record.get('content_html', '')
            code_examples = record.get('code_examples', [])
            
            # 生成 Markdown 内容
            markdown_content = self._generate_markdown(
                title=title,
                url=url,
                breadcrumb=breadcrumb,
                content_html=content_html,
                code_examples=code_examples
            )
            
            # 生成文件路径
            filepath = self._generate_filepath(url, category, title)
            
            return {
                'filepath': filepath,
                'markdown': markdown_content,
                'title': title,
                'url': url,
                'category': category
            }
            
        except Exception as e:
            logger.error(f"转换页面失败: {record.get('url')}, 错误: {str(e)}")
            return None
            
    def _generate_markdown(self, title: str, url: str, breadcrumb: list, 
                          content_html: str, code_examples: list) -> str:
        """
        生成 Markdown 内容
        
        Args:
            title: 标题
            url: URL
            breadcrumb: 面包屑
            content_html: HTML 内容
            code_examples: 代码示例
            
        Returns:
            Markdown 字符串
        """
        parts = []
        
        # 添加 YAML 前置元数据
        parts.append("---")
        parts.append(f"title: {title}")
        parts.append(f"url: {url}")
        if breadcrumb:
            parts.append(f"breadcrumb: {' > '.join(breadcrumb)}")
        parts.append("---")
        parts.append("")
        
        # 添加标题
        parts.append(f"# {title}")
        parts.append("")
        
        # 转换 HTML 为 Markdown
        if content_html:
            markdown_body = self._html_to_markdown(content_html)
            parts.append(markdown_body)
            parts.append("")
            
        # 添加代码示例部分（如果有且未在正文中）
        if code_examples and not self._has_code_blocks(content_html):
            parts.append("## 代码示例")
            parts.append("")
            
            for i, example in enumerate(code_examples, 1):
                if example.get('description'):
                    parts.append(f"### 示例 {i}: {example['description']}")
                    parts.append("")
                    
                language = example.get('language', 'text')
                code = example.get('code', '')
                parts.append(f"```{language}")
                parts.append(code)
                parts.append("```")
                parts.append("")
                
        return "\n".join(parts)
        
    def _html_to_markdown(self, html: str) -> str:
        """
        HTML 转 Markdown
        
        Args:
            html: HTML 字符串
            
        Returns:
            Markdown 字符串
        """
        # 使用 markdownify 转换
        markdown = md(
            html,
            heading_style="ATX",  # 使用 # 风格的标题
            bullets="-",  # 使用 - 作为列表符号
            code_language="",  # 保留代码块语言标记
            strip=['script', 'style']  # 移除 script 和 style 标签
        )
        
        # 清理转换结果
        markdown = self._clean_markdown(markdown)
        
        return markdown
        
    def _clean_markdown(self, markdown: str) -> str:
        """清理 Markdown 文本"""
        # 移除多余的空行（超过2个连续空行）
        markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)
        
        # 清理代码块中的多余空行
        markdown = re.sub(r'```(\w*)\n\n+', r'```\1\n', markdown)
        
        # 确保代码块结束后有空行
        markdown = re.sub(r'```\n([^`])', r'```\n\n\1', markdown)
        
        # 清理表格格式
        markdown = re.sub(r'\|  +\|', '| |', markdown)
        
        return markdown.strip()
        
    def _has_code_blocks(self, html: str) -> bool:
        """检查 HTML 中是否包含代码块"""
        soup = BeautifulSoup(html, 'lxml')
        return bool(soup.find_all(['pre', 'code']))
        
    def _generate_filepath(self, url: str, category: str, title: str) -> Path:
        """
        生成文件路径
        
        Args:
            url: URL
            category: 分类
            title: 标题
            
        Returns:
            文件路径
        """
        # 从 URL 提取路径信息
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        url_path = parsed_url.path.strip('/')
        url_parts = [p for p in url_path.split('/') if p]  # 过滤空字符串
        
        # 创建分类目录
        category_dir = self.output_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成文件名和子目录
        filename = None
        sub_dir = None
        
        # 从 URL 路径提取文件名和子目录
        if url_parts:
            # 最后一个非空部分作为文件名
            filename = url_parts[-1] if url_parts[-1] else None
            
            # 倒数第2-3个部分作为子目录
            if len(url_parts) >= 2:
                sub_parts = [p for p in url_parts[-3:-1] if p and p not in ('doc', 'common')]
                if sub_parts:
                    sub_dir = '/'.join(sub_parts)
        
        # 如果没有有效文件名，使用标题
        if not filename or filename in ('doc', 'common'):
            filename = self._sanitize_filename(title)
        
        # 确保文件名不为空且符合命名规范
        if not filename:
            filename = 'untitled'
        else:
            # 转换为小写并用短横线连接（如果包含特殊字符）
            filename = self._normalize_filename(filename)
        
        # 构建完整路径
        if sub_dir:
            full_sub_dir = category_dir / sub_dir
            full_sub_dir.mkdir(parents=True, exist_ok=True)
            filepath = full_sub_dir / f"{filename}.md"
        else:
            filepath = category_dir / f"{filename}.md"
        
        return filepath
        
    def _sanitize_filename(self, filename: str) -> str:
        """清理文件名，移除非法字符"""
        # 移除或替换非法字符
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # 替换空格为短横线
        filename = filename.replace(' ', '-')
        # 限制长度
        if len(filename) > 100:
            filename = filename[:100]
        return filename or 'untitled'
    
    def _normalize_filename(self, filename: str) -> str:
        """标准化文件名为小写短横线格式"""
        # 先清理非法字符
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # 将驼峰命名转换为短横线（例如：localStorage -> local-storage）
        filename = re.sub(r'([a-z])([A-Z])', r'\1-\2', filename)
        # 替换空格、下划线为短横线
        filename = re.sub(r'[\s_]+', '-', filename)
        # 转换为小写
        filename = filename.lower()
        # 移除多余的短横线
        filename = re.sub(r'-+', '-', filename)
        # 移除首尾短横线
        filename = filename.strip('-')
        # 限制长度
        if len(filename) > 100:
            filename = filename[:100].rstrip('-')
        return filename or 'untitled'
        
    def save_markdown(self, filepath: Path, content: str):
        """
        保存 Markdown 文件
        
        Args:
            filepath: 文件路径
            content: Markdown 内容
        """
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.debug(f"保存 Markdown: {filepath}")
        except Exception as e:
            logger.error(f"保存 Markdown 失败: {filepath}, 错误: {str(e)}")
