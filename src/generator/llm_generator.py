"""
LLM 文档生成器

生成适合大模型理解和使用的文档格式
"""

import json
import logging
import re
from pathlib import Path
from typing import List, Dict
from collections import defaultdict

logger = logging.getLogger(__name__)


class LLMDocGenerator:
    """LLM 文档生成器"""
    
    def __init__(self, output_dir: str = "output/llm-ready"):
        """
        初始化生成器
        
        Args:
            output_dir: 输出目录
        """
        self.output_dir = Path(output_dir)
        self.combined_dir = self.output_dir / "combined"
        self.qa_dir = self.output_dir / "qa-pairs"
        
        self.combined_dir.mkdir(parents=True, exist_ok=True)
        self.qa_dir.mkdir(parents=True, exist_ok=True)
        
    def process_markdown_files(self, markdown_dir: Path):
        """
        处理所有 Markdown 文件
        
        Args:
            markdown_dir: Markdown 文件目录
        """
        logger.info("开始生成 LLM 就绪文档...")
        
        # 按分类收集文档
        docs_by_category = defaultdict(list)
        
        for md_file in markdown_dir.rglob("*.md"):
            # 确定分类
            relative_path = md_file.relative_to(markdown_dir)
            category = relative_path.parts[0] if relative_path.parts else 'other'
            
            # 读取文档
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            docs_by_category[category].append({
                'filepath': md_file,
                'relative_path': str(relative_path),
                'content': content
            })
            
        # 为每个分类生成合并文档
        for category, docs in docs_by_category.items():
            logger.info(f"处理分类: {category} ({len(docs)} 个文档)")
            self._generate_combined_doc(category, docs)
            
        logger.info("LLM 文档生成完成")
        
    def _generate_combined_doc(self, category: str, docs: List[Dict]):
        """
        生成合并文档
        
        Args:
            category: 分类名称
            docs: 文档列表
        """
        # 排序文档（按路径）
        docs.sort(key=lambda x: x['relative_path'])
        
        # 生成目录
        toc = self._generate_table_of_contents(docs)
        
        # 合并所有文档
        combined_content = []
        
        # 添加总标题和说明
        combined_content.append(f"# vivo BlueOS 手表开发文档 - {self._category_name(category)}")
        combined_content.append("")
        combined_content.append(f"> 本文档由爬虫自动生成，包含 {len(docs)} 个页面的内容")
        combined_content.append("")
        
        # 添加目录
        combined_content.append("## 目录")
        combined_content.append("")
        combined_content.extend(toc)
        combined_content.append("")
        combined_content.append("---")
        combined_content.append("")
        
        # 添加所有文档内容
        for i, doc in enumerate(docs, 1):
            content = doc['content']
            
            # 移除 YAML 前置元数据
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            
            # 调整标题级别（所有标题降一级）
            content = self._adjust_heading_levels(content)
            
            # 添加分隔符
            combined_content.append(f"\n<!-- 文档 {i}: {doc['relative_path']} -->")
            combined_content.append("")
            combined_content.append(content)
            combined_content.append("")
            combined_content.append("---")
            combined_content.append("")
            
        # 保存合并文档
        output_file = self.combined_dir / f"{category}-complete.md"
        combined_text = "\n".join(combined_content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(combined_text)
            
        logger.info(f"保存合并文档: {output_file} ({len(combined_text)} 字符)")
        
    def _generate_table_of_contents(self, docs: List[Dict]) -> List[str]:
        """生成目录"""
        toc = []
        
        for doc in docs:
            content = doc['content']
            relative_path = doc['relative_path']
            
            # 提取第一个标题
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
            else:
                title = relative_path
                
            # 生成锚点
            anchor = self._generate_anchor(title)
            toc.append(f"- [{title}](#{anchor})")
            
        return toc
        
    def _adjust_heading_levels(self, content: str) -> str:
        """调整标题级别（降一级）"""
        # 将 # 替换为 ##，## 替换为 ###，以此类推
        def replace_heading(match):
            hashes = match.group(1)
            title = match.group(2)
            return f"#{hashes} {title}"
            
        return re.sub(r'^(#{1,5})\s+(.+)$', replace_heading, content, flags=re.MULTILINE)
        
    def _generate_anchor(self, title: str) -> str:
        """生成 Markdown 锚点"""
        # 转换为小写
        anchor = title.lower()
        # 替换空格和特殊字符
        anchor = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        return anchor
        
    def _category_name(self, category: str) -> str:
        """获取分类中文名称"""
        names = {
            'tutorial': '教程文档',
            'js-api': 'JavaScript API',
            'ui-component': 'UI 组件'
        }
        return names.get(category, category)
        
    def generate_qa_pairs(self, data_dir: Path):
        """
        生成问答对数据集
        
        Args:
            data_dir: 数据目录
        """
        logger.info("开始生成问答对数据集...")
        
        qa_pairs = []
        
        # 读取所有原始数据
        raw_dir = data_dir / "raw"
        for jsonl_file in raw_dir.glob("*.jsonl"):
            with open(jsonl_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        record = json.loads(line)
                        if record.get('status') == 'success':
                            qa_pairs.extend(self._extract_qa_from_record(record))
                            
        # 保存问答对
        output_file = self.qa_dir / "qa-dataset.jsonl"
        with open(output_file, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa, ensure_ascii=False) + '\n')
                
        logger.info(f"生成问答对: {len(qa_pairs)} 条 -> {output_file}")
        
    def _extract_qa_from_record(self, record: dict) -> List[Dict]:
        """从记录中提取问答对"""
        qa_pairs = []
        
        title = record.get('title', '')
        url = record.get('url', '')
        content_text = record.get('content_text', '')
        code_examples = record.get('code_examples', [])
        
        if not title:
            return qa_pairs
            
        # 概念理解型问答
        if content_text:
            # 提取前200个字符作为摘要
            summary = content_text[:200].strip()
            if summary:
                qa_pairs.append({
                    'question': f"{title}是什么？",
                    'answer': summary,
                    'type': 'concept',
                    'source_url': url
                })
                
        # 代码示例型问答
        for i, example in enumerate(code_examples):
            code = example.get('code', '')
            language = example.get('language', 'javascript')
            description = example.get('description', '')
            
            if code:
                question = f"如何使用{title}？" if i == 0 else f"{title}的使用示例{i+1}"
                answer = f"{description}\n\n```{language}\n{code}\n```" if description else f"```{language}\n{code}\n```"
                
                qa_pairs.append({
                    'question': question,
                    'answer': answer,
                    'type': 'example',
                    'source_url': url,
                    'language': language
                })
                
        return qa_pairs
