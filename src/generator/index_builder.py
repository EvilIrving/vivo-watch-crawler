"""
文档索引构建器

为 MCP 服务准备结构化索引数据
"""

import json
import logging
import re
from pathlib import Path
from typing import List, Dict
from collections import defaultdict

logger = logging.getLogger(__name__)


class IndexBuilder:
    """文档索引构建器"""
    
    def __init__(self, output_dir: str = "output/index"):
        """
        初始化索引构建器
        
        Args:
            output_dir: 输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def build_all_indexes(self, data_dir: Path, markdown_dir: Path):
        """
        构建所有索引
        
        Args:
            data_dir: 数据目录
            markdown_dir: Markdown 目录
        """
        logger.info("开始构建索引...")
        
        # 读取原始数据
        records = self._load_all_records(data_dir / "raw")
        
        # 构建文档索引
        doc_index = self._build_doc_index(records, markdown_dir)
        self._save_index('doc-index.json', doc_index)
        
        # 构建 API 索引
        api_index = self._build_api_index(records)
        self._save_index('api-index.json', api_index)
        
        # 构建组件索引
        component_index = self._build_component_index(records)
        self._save_index('component-index.json', component_index)
        
        # 构建代码示例索引
        code_index = self._build_code_examples_index(records)
        self._save_index('code-examples-index.json', code_index)
        
        logger.info("索引构建完成")
        
    def _load_all_records(self, raw_dir: Path) -> List[Dict]:
        """加载所有原始记录"""
        records = []
        
        for jsonl_file in raw_dir.glob("*.jsonl"):
            with open(jsonl_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        record = json.loads(line)
                        if record.get('status') == 'success':
                            records.append(record)
                            
        logger.info(f"加载记录: {len(records)} 条")
        return records
        
    def _build_doc_index(self, records: List[Dict], markdown_dir: Path) -> Dict:
        """构建文档索引"""
        doc_index = {
            'total': len(records),
            'categories': defaultdict(list),
            'documents': []
        }
        
        for i, record in enumerate(records):
            url = record.get('url', '')
            title = record.get('title', '')
            category = record.get('category', 'other')
            breadcrumb = record.get('breadcrumb', [])
            content_text = record.get('content_text', '')
            
            # 生成文档 ID
            doc_id = f"doc_{i:04d}"
            
            # 提取关键词
            keywords = self._extract_keywords(title, content_text)
            
            # 生成摘要
            summary = content_text[:200].strip() if content_text else ""
            
            doc_entry = {
                'id': doc_id,
                'title': title,
                'url': url,
                'category': category,
                'breadcrumb': breadcrumb,
                'summary': summary,
                'keywords': keywords,
                'has_code': len(record.get('code_examples', [])) > 0
            }
            
            doc_index['documents'].append(doc_entry)
            doc_index['categories'][category].append(doc_id)
            
        # 转换 defaultdict 为普通 dict
        doc_index['categories'] = dict(doc_index['categories'])
        
        return doc_index
        
    def _build_api_index(self, records: List[Dict]) -> Dict:
        """构建 API 索引"""
        api_index = {
            'total': 0,
            'apis': []
        }
        
        for record in records:
            if record.get('category') != 'js-api':
                continue
                
            title = record.get('title', '')
            url = record.get('url', '')
            content_text = record.get('content_text', '')
            code_examples = record.get('code_examples', [])
            
            # 提取 API 名称（通常在标题或 URL 中）
            api_name = self._extract_api_name(title, url)
            
            if not api_name:
                continue
                
            # 提取参数信息
            parameters = self._extract_parameters(content_text)
            
            # 提取返回值信息
            returns = self._extract_returns(content_text)
            
            api_entry = {
                'name': api_name,
                'title': title,
                'url': url,
                'namespace': self._extract_namespace(url),
                'parameters': parameters,
                'returns': returns,
                'examples_count': len(code_examples),
                'description': content_text[:300].strip() if content_text else ""
            }
            
            api_index['apis'].append(api_entry)
            
        api_index['total'] = len(api_index['apis'])
        return api_index
        
    def _build_component_index(self, records: List[Dict]) -> Dict:
        """构建组件索引"""
        component_index = {
            'total': 0,
            'components': []
        }
        
        for record in records:
            if record.get('category') != 'ui-component':
                continue
                
            title = record.get('title', '')
            url = record.get('url', '')
            content_text = record.get('content_text', '')
            code_examples = record.get('code_examples', [])
            
            # 提取组件名称
            component_name = self._extract_component_name(title, url)
            
            if not component_name:
                continue
                
            # 提取属性列表
            attributes = self._extract_attributes(content_text)
            
            # 提取事件列表
            events = self._extract_events(content_text)
            
            component_entry = {
                'name': component_name,
                'title': title,
                'url': url,
                'type': self._classify_component(url),
                'attributes': attributes,
                'events': events,
                'examples_count': len(code_examples),
                'description': content_text[:300].strip() if content_text else ""
            }
            
            component_index['components'].append(component_entry)
            
        component_index['total'] = len(component_index['components'])
        return component_index
        
    def _build_code_examples_index(self, records: List[Dict]) -> Dict:
        """构建代码示例索引"""
        code_index = {
            'total': 0,
            'examples': []
        }
        
        example_id = 0
        
        for record in records:
            url = record.get('url', '')
            title = record.get('title', '')
            code_examples = record.get('code_examples', [])
            
            for example in code_examples:
                example_id += 1
                
                code_entry = {
                    'id': f"example_{example_id:04d}",
                    'code': example.get('code', ''),
                    'language': example.get('language', 'text'),
                    'description': example.get('description', ''),
                    'source_title': title,
                    'source_url': url,
                    'category': record.get('category', 'other')
                }
                
                code_index['examples'].append(code_entry)
                
        code_index['total'] = len(code_index['examples'])
        return code_index
        
    def _extract_keywords(self, title: str, content: str) -> List[str]:
        """提取关键词"""
        keywords = []
        
        # 从标题提取
        if title:
            keywords.append(title)
            
        # 提取常见技术词汇
        tech_words = re.findall(r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)*\b', content)
        keywords.extend(tech_words[:5])
        
        return list(set(keywords))[:10]
        
    def _extract_api_name(self, title: str, url: str) -> str:
        """提取 API 名称"""
        # 从 URL 提取
        parts = url.split('/')
        if parts:
            return parts[-1]
        return title
        
    def _extract_namespace(self, url: str) -> str:
        """提取命名空间"""
        match = re.search(r'/js/(\w+)/', url)
        if match:
            return match.group(1)
        return ""
        
    def _extract_parameters(self, content: str) -> List[Dict]:
        """提取参数信息（简单实现）"""
        parameters = []
        
        # 查找参数表格或列表
        param_patterns = [
            r'参数[：:]\s*(\w+)',
            r'name[：:]\s*(\w+)',
            r'@param\s+(\w+)'
        ]
        
        for pattern in param_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches[:10]:  # 限制数量
                parameters.append({'name': match})
                
        return parameters
        
    def _extract_returns(self, content: str) -> str:
        """提取返回值信息"""
        # 查找返回值说明
        return_patterns = [
            r'返回值[：:]\s*(.+)',
            r'return[s]?[：:]\s*(.+)',
            r'@returns?\s+(.+)'
        ]
        
        for pattern in return_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1)[:200]
                
        return ""
        
    def _extract_component_name(self, title: str, url: str) -> str:
        """提取组件名称"""
        # 从 URL 或标题提取
        parts = url.split('/')
        if parts:
            return parts[-1]
        return title
        
    def _classify_component(self, url: str) -> str:
        """分类组件类型"""
        if '/basic/' in url:
            return 'basic'
        elif '/form/' in url:
            return 'form'
        elif '/layout/' in url or '/container/' in url:
            return 'layout'
        elif '/navigation/' in url:
            return 'navigation'
        elif '/animation/' in url:
            return 'animation'
        else:
            return 'common'
            
    def _extract_attributes(self, content: str) -> List[str]:
        """提取属性列表"""
        # 简单实现：查找属性关键词
        attrs = re.findall(r'(?:属性|attribute|prop)[：:]\s*(\w+)', content, re.IGNORECASE)
        return list(set(attrs))[:20]
        
    def _extract_events(self, content: str) -> List[str]:
        """提取事件列表"""
        # 简单实现：查找事件关键词
        events = re.findall(r'(?:事件|event)[：:]\s*(\w+)', content, re.IGNORECASE)
        return list(set(events))[:20]
        
    def _save_index(self, filename: str, index: Dict):
        """保存索引文件"""
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
            
        logger.info(f"保存索引: {filename}")
