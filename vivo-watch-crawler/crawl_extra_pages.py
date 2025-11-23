#!/usr/bin/env python3
"""爬取额外的 practice 页面"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from pathlib import Path

# 要爬取的额外页面
extra_urls = [
    'https://studio.blueos.com.cn/practice/zustand-guide/',
    'https://studio.blueos.com.cn/practice/watch-guide/',
    'https://studio.blueos.com.cn/practice/tailwind-css/',
    'https://studio.blueos.com.cn/practice/settimeout-guide/'
]

# 创建 data/raw 目录
data_dir = Path('data/raw')
data_dir.mkdir(parents=True, exist_ok=True)

# 保存到 tutorial.jsonl（因为这些是实践指南）
output_file = data_dir / 'tutorial.jsonl'

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
})

success_count = 0
for url in extra_urls:
    try:
        print(f'正在爬取: {url}')
        
        # 请求页面
        response = session.get(url, timeout=30)
        response.raise_for_status()
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取标题
        title = ''
        h1 = soup.find('h1')
        if h1:
            title = h1.get_text(strip=True)
        
        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text(strip=True)
        
        # 提取主内容（尝试多个选择器）
        content_div = None
        for selector in ['.html-content', 'article', 'main', '.content', '.markdown-body']:
            content_div = soup.select_one(selector)
            if content_div:
                break
        
        if not content_div:
            # 如果没找到特定容器，使用整个 body
            content_div = soup.find('body')
        
        html_content = str(content_div) if content_div else ''
        text_content = content_div.get_text(separator='\n', strip=True) if content_div else ''
        
        # 提取代码示例
        code_examples = []
        if content_div:
            for i, pre in enumerate(content_div.find_all('pre')):
                code_tag = pre.find('code')
                if code_tag:
                    code_text = code_tag.get_text()
                    language = 'text'
                    class_attr = code_tag.get('class', [])
                    for cls in class_attr:
                        if 'language-' in str(cls):
                            language = str(cls).replace('language-', '')
                            break
                    
                    code_examples.append({
                        'code': code_text.strip(),
                        'language': language,
                        'index': i
                    })
        
        # 构建记录
        record = {
            'url': url,
            'category': 'tutorial',
            'crawl_time': datetime.now().isoformat(),
            'status': 'success',
            'title': title,
            'breadcrumb': [],
            'content_html': html_content,
            'content_text': text_content,
            'code_examples': code_examples,
            'frontmatter': {'title': title},
            'has_content': bool(html_content and text_content)
        }
        
        # 追加到文件
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
        
        print(f'  ✓ 成功: {title}')
        print(f'     HTML: {len(html_content)} 字符')
        print(f'     代码示例: {len(code_examples)} 个')
        success_count += 1
        
    except Exception as e:
        print(f'  ✗ 失败: {str(e)}')

print(f'\n完成！成功爬取 {success_count}/{len(extra_urls)} 个页面')
print(f'数据已保存到: {output_file}')
