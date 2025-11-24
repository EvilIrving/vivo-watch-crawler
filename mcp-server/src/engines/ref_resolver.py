"""
快速引用解析器

解析引用标识符(如 @blueos-api.json)并定位资源文件
"""

import json
import re
from pathlib import Path
from typing import Optional, Dict, Any


class RefResolver:
    def __init__(self, refs_file: str, base_dir: str):
        """
        初始化引用解析器
        
        Args:
            refs_file: 引用映射表文件路径
            base_dir: 基础目录路径
        """
        self.refs_file = Path(refs_file)
        self.base_dir = Path(base_dir)
        self.refs_data = {}
        self.patterns = []
        self.load()
    
    def load(self):
        """加载引用映射表"""
        if not self.refs_file.exists():
            raise FileNotFoundError(f"引用映射表不存在: {self.refs_file}")
        
        with open(self.refs_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.refs_data = data.get('refs', {})
            self.patterns = data.get('patterns', [])
    
    def resolve(self, ref: str) -> Optional[Dict[str, Any]]:
        """
        解析引用标识符
        
        Args:
            ref: 引用标识符,如 '@blueos-api.json'
            
        Returns:
            包含文件路径和元数据的字典,如果未找到则返回None
        """
        # 验证格式
        if not ref.startswith('@blueos-'):
            return None
        
        # 1. 尝试静态引用匹配
        if ref in self.refs_data:
            ref_info = self.refs_data[ref].copy()
            file_path = self.base_dir / ref_info['path']
            
            if not file_path.exists():
                return None
            
            ref_info['absolute_path'] = str(file_path)
            return ref_info
        
        # 2. 尝试模式匹配
        for pattern_info in self.patterns:
            pattern = pattern_info['pattern']
            template = pattern_info['template']
            
            match = re.match(pattern, ref)
            if match:
                # 提取参数
                params = match.groups()
                
                # 填充模板路径
                try:
                    relative_path = template.format(*params)
                except (IndexError, KeyError):
                    continue
                
                # 处理通配符路径
                if '**' in relative_path:
                    # 使用glob查找文件
                    file_path = self._find_with_glob(relative_path, params[0])
                else:
                    file_path = self.base_dir / relative_path
                
                if file_path and file_path.exists():
                    return {
                        'path': str(file_path.relative_to(self.base_dir)),
                        'absolute_path': str(file_path),
                        'type': self._get_mime_type(file_path),
                        'description': pattern_info['description'],
                        'category': 'pattern',
                        'size': file_path.stat().st_size
                    }
        
        return None
    
    def _find_with_glob(self, pattern: str, target: str) -> Optional[Path]:
        """
        使用glob查找匹配的文件
        
        Args:
            pattern: 包含通配符的路径模式
            target: 目标文件名
            
        Returns:
            找到的文件路径,如果未找到则返回None
        """
        # 将模式转换为glob模式
        glob_pattern = pattern.replace('{0}', target)
        
        # 在基础目录下搜索
        for file_path in self.base_dir.rglob(f"{target}.md"):
            if 'component' in str(file_path):
                return file_path
        
        return None
    
    def _get_mime_type(self, file_path: Path) -> str:
        """获取MIME类型"""
        ext = file_path.suffix.lower()
        # 处理 .d.ts 的双扩展名
        if file_path.name.endswith('.d.ts'):
            return 'application/typescript'
        
        mime_types = {
            '.json': 'application/json',
            '.md': 'text/markdown',
            '.txt': 'text/plain',
            '.ts': 'application/typescript',
            '.js': 'application/javascript'
        }
        return mime_types.get(ext, 'application/octet-stream')
    
    def list_refs(self, category: Optional[str] = None) -> Dict[str, Any]:
        """
        列出所有可用的引用
        
        Args:
            category: 可选的分类过滤
            
        Returns:
            引用列表
        """
        if category:
            return {
                ref: info for ref, info in self.refs_data.items()
                if info.get('category') == category
            }
        return self.refs_data.copy()
