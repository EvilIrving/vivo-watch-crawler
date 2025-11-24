"""
文档搜索引擎

实现关键词搜索和语义匹配功能
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional


class SearchEngine:
    # TypeScript 特定的查询关键词映射
    TS_QUERY_PATTERNS = {
        'interface': ['interface', '接口'],
        'type': ['type', '类型', 'typedef'],
        'class': ['class', '类'],
        'function': ['function', '函数'],
        'method': ['method', '方法'],
        'enum': ['enum', '枚举'],
        'property': ['property', '属性', 'prop'],
        'api': ['api', 'interface', 'method', 'function']
    }
    
    def __init__(self, doc_index_file: str):
        """
        初始化搜索引擎
        
        Args:
            doc_index_file: 文档索引文件路径
        """
        self.doc_index_file = Path(doc_index_file)
        self.documents = []
        self.keyword_index = {}  # 倒排索引: keyword -> [doc_ids]
        self.category_index = {}  # 分类索引: category -> [doc_ids]
        self.type_info_index = {}  # 类型信息索引: type_element -> [doc_ids]
        self.load_index()
    
    def load_index(self):
        """加载文档索引"""
        if not self.doc_index_file.exists():
            raise FileNotFoundError(f"文档索引不存在: {self.doc_index_file}")
        
        with open(self.doc_index_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.documents = data.get('documents', [])
        
        # 构建倒排索引
        self._build_keyword_index()
        self._build_category_index()
        self._build_type_info_index()
    
    def _build_keyword_index(self):
        """构建关键词倒排索引"""
        for doc in self.documents:
            doc_id = doc['id']
            
            # 索引标题
            if 'title' in doc:
                for word in self._tokenize(doc['title']):
                    if word not in self.keyword_index:
                        self.keyword_index[word] = []
                    if doc_id not in self.keyword_index[word]:
                        self.keyword_index[word].append(doc_id)
            
            # 索引关键词
            if 'keywords' in doc:
                for keyword in doc['keywords']:
                    for word in self._tokenize(keyword):
                        if word not in self.keyword_index:
                            self.keyword_index[word] = []
                        if doc_id not in self.keyword_index[word]:
                            self.keyword_index[word].append(doc_id)
    
    def _build_category_index(self):
        """构建分类索引"""
        for doc in self.documents:
            category = doc.get('category', 'unknown')
            if category not in self.category_index:
                self.category_index[category] = []
            self.category_index[category].append(doc['id'])
    
    def _build_type_info_index(self):
        """构建 TypeScript 类型信息索引（用于 .d.ts 文件）"""
        for doc in self.documents:
            # 只索引 TypeScript 定义文件
            if doc.get('category') != 'typescript-definitions':
                continue
            
            doc_id = doc['id']
            type_info = doc.get('type_info', {})
            
            # 索引接口、类、函数、枚举、类型等
            for type_element in type_info.get('interfaces', []):
                if 'interface' not in self.type_info_index:
                    self.type_info_index['interface'] = []
                if doc_id not in self.type_info_index['interface']:
                    self.type_info_index['interface'].append(doc_id)
                # 也索引具体的接口名称
                key = f"interface:{type_element.lower()}"
                if key not in self.type_info_index:
                    self.type_info_index[key] = []
                if doc_id not in self.type_info_index[key]:
                    self.type_info_index[key].append(doc_id)
            
            for type_element in type_info.get('classes', []):
                if 'class' not in self.type_info_index:
                    self.type_info_index['class'] = []
                if doc_id not in self.type_info_index['class']:
                    self.type_info_index['class'].append(doc_id)
            
            for type_element in type_info.get('functions', []):
                if 'function' not in self.type_info_index:
                    self.type_info_index['function'] = []
                if doc_id not in self.type_info_index['function']:
                    self.type_info_index['function'].append(doc_id)
            
            for type_element in type_info.get('types', []):
                if 'type' not in self.type_info_index:
                    self.type_info_index['type'] = []
                if doc_id not in self.type_info_index['type']:
                    self.type_info_index['type'].append(doc_id)
            
            for type_element in type_info.get('enums', []):
                if 'enum' not in self.type_info_index:
                    self.type_info_index['enum'] = []
                if doc_id not in self.type_info_index['enum']:
                    self.type_info_index['enum'].append(doc_id)
    
    def _tokenize(self, text: str) -> List[str]:
        """分词"""
        # 简单分词: 转小写,按非字母数字字符分割
        import re
        tokens = re.findall(r'\w+', text.lower())
        return tokens
    
    def _is_typescript_query(self, query_tokens: List[str]) -> bool:
        """判断查询是否是 TypeScript/API 相关查询"""
        query_lower = ' '.join(query_tokens).lower()
        # 检查是否包含 TS 相关关键词
        for pattern_group in self.TS_QUERY_PATTERNS.values():
            for pattern in pattern_group:
                if pattern in query_lower:
                    return True
        return False
    
    def search(
        self,
        query: str,
        category: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        搜索文档
        
        Args:
            query: 搜索查询
            category: 可选的分类过滤
            limit: 返回结果数量限制
            
        Returns:
            匹配的文档列表,按相关度排序
        """
        results = []
        query_tokens = self._tokenize(query)
        
        # 如果没有有效的查询关键词，返回空结果
        if not query_tokens:
            return results
        
        # 如果指定了分类,先过滤
        candidate_doc_ids = None
        if category and category != 'all':
            candidate_doc_ids = set(self.category_index.get(category, []))
            # 如果指定的分类不存在，返回空结果
            if not candidate_doc_ids:
                return results
        
        # 计算每个文档的相关度得分
        doc_scores = {}
        
        for doc in self.documents:
            doc_id = doc['id']
            
            # 分类过滤
            if candidate_doc_ids is not None and doc_id not in candidate_doc_ids:
                continue
            
            score = self._calculate_relevance(doc, query_tokens)
            if score > 0:
                doc_scores[doc_id] = score
        
        # 如果没有任何匹配，尝试降低门槛，返回部分匹配的结果
        if not doc_scores:
            for doc in self.documents:
                doc_id = doc['id']
                
                # 分类过滤
                if candidate_doc_ids is not None and doc_id not in candidate_doc_ids:
                    continue
                
                # 使用更宽松的匹配：只要摘要中包含任一关键词
                summary = doc.get('summary', '').lower()
                title = doc.get('title', '').lower()
                
                partial_score = 0.0
                for token in query_tokens:
                    if len(token) > 2 and (token in summary or token in title):
                        partial_score += 0.3
                
                if partial_score > 0:
                    doc_scores[doc_id] = partial_score
        
        # 排序并限制结果数量
        sorted_doc_ids = sorted(
            doc_scores.keys(),
            key=lambda x: doc_scores[x],
            reverse=True
        )[:limit]
        
        # 构建结果
        for doc_id in sorted_doc_ids:
            doc = self._get_doc_by_id(doc_id)
            if doc:
                result = {
                    'title': doc.get('title', ''),
                    'category': doc.get('category', ''),
                    'url': doc.get('url', ''),
                    'ref': self._generate_ref(doc),
                    'summary': doc.get('summary', '')[:200] + '...' if len(doc.get('summary', '')) > 200 else doc.get('summary', ''),
                    'relevance': doc_scores[doc_id]
                }
                results.append(result)
        
        return results
    
    def _calculate_relevance(self, doc: Dict[str, Any], query_tokens: List[str]) -> float:
        """
        计算文档相关度得分
        
        Args:
            doc: 文档
            query_tokens: 查询关键词列表
            
        Returns:
            相关度得分
        """
        score = 0.0
        
        title = doc.get('title', '').lower()
        summary = doc.get('summary', '').lower()
        keywords = [k.lower() for k in doc.get('keywords', [])]
        url = doc.get('url', '').lower()
        category = doc.get('category', '')
        
        # 检查是否是 TypeScript 查询
        is_ts_query = self._is_typescript_query(query_tokens)
        
        # 遍历每个查询关键词
        for token in query_tokens:
            # 跳过过短的词（如 a, or, and 等）
            if len(token) <= 1:
                continue
            
            # 精确匹配标题 - 高权重
            if token in title:
                score += 2.0
            
            # 精确匹配关键词 - 高权重
            if token in keywords:
                score += 1.5
            # 部分匹配关键词
            elif any(token in kw for kw in keywords):
                score += 0.8
            
            # 匹配 URL 路径
            if token in url:
                score += 1.0
            
            # 匹配摘要 - 基础权重
            if token in summary:
                score += 0.5
        
        # TypeScript 查询加权
        if is_ts_query:
            # 如果是 TS 查询，且文档是 .d.ts 文件，增加权重
            if category == 'typescript-definitions':
                score += 2.0
            
            # 检查是否在 type_info 中有匹配
            type_info = doc.get('type_info', {})
            for token in query_tokens:
                # 在接口中查找
                if token in [i.lower() for i in type_info.get('interfaces', [])]:
                    score += 1.5
                # 在函数中查找
                elif token in [f.lower() for f in type_info.get('functions', [])]:
                    score += 1.5
                # 在类中查找
                elif token in [c.lower() for c in type_info.get('classes', [])]:
                    score += 1.0
                # 在类型中查找
                elif token in [t.lower() for t in type_info.get('types', [])]:
                    score += 1.0
        
        # 分类加权
        if any(token in category for token in query_tokens):
            score += 0.3
        
        # 如果查询词数量较多，且部分匹配，给予额外加分
        if len(query_tokens) >= 3 and score > 0:
            score += 0.5
        
        return score
    
    def _get_doc_by_id(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """根据ID获取文档"""
        for doc in self.documents:
            if doc['id'] == doc_id:
                return doc
        return None
    
    def _generate_ref(self, doc: Dict[str, Any]) -> str:
        """生成文档的快速引用标识符"""
        category = doc.get('category', '')
        title = doc.get('title', '').lower().replace(' ', '-')
        
        # 处理 TypeScript 类型定义
        if category == 'typescript-definitions':
            # 对于 .d.ts 文件，使用完整路径
            path_info = doc.get('path', '')
            if path_info:
                return f"@blueos-api/{path_info.replace('data/api/', '').replace('.d.ts', '')}.d.ts"
            return f"@blueos-api/{title}.d.ts"
        
        if category == 'js-api':
            return f"@blueos-api/{title}.md"
        elif category == 'ui-component':
            return f"@blueos-component/{title}.md"
        elif category == 'tutorial':
            return f"@blueos-tutorial/{title}.md"
        else:
            return f"@blueos-doc/{title}.md"
    
    def get_by_category(self, category: str) -> List[Dict[str, Any]]:
        """获取指定分类的所有文档"""
        doc_ids = self.category_index.get(category, [])
        return [self._get_doc_by_id(doc_id) for doc_id in doc_ids if self._get_doc_by_id(doc_id)]
