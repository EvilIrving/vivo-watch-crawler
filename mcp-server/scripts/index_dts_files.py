#!/usr/bin/env python3
"""
索引 TypeScript 类型定义文件

扫描 data/api 目录下的所有 .d.ts 文件，
为文档索引和搜索引擎生成相关数据
"""

import json
import re
from pathlib import Path
from typing import List, Dict


class DtsIndexer:
    def __init__(self, data_dir: str, index_dir: str):
        """
        初始化 .d.ts 索引器
        
        Args:
            data_dir: 数据目录 (包含 api/)
            index_dir: 索引输出目录
        """
        self.data_dir = Path(data_dir)
        self.index_dir = Path(index_dir)
        self.documents = []
        self.dts_files = []
    
    def discover_dts_files(self) -> List[Path]:
        """发现所有 .d.ts 文件"""
        api_dir = self.data_dir / "api"
        if not api_dir.exists():
            return []
        
        files = list(api_dir.rglob("*.d.ts"))
        self.dts_files = sorted(files)
        return self.dts_files
    
    def extract_type_definitions(self, content: str) -> Dict:
        """从 .d.ts 文件提取类型定义信息"""
        info = {
            'interfaces': [],
            'classes': [],
            'enums': [],
            'types': [],
            'functions': []
        }
        
        # 提取接口定义
        interfaces = re.findall(r'export\s+interface\s+(\w+)', content)
        info['interfaces'] = interfaces
        
        # 提取类定义
        classes = re.findall(r'export\s+class\s+(\w+)', content)
        info['classes'] = classes
        
        # 提取枚举定义
        enums = re.findall(r'export\s+enum\s+(\w+)', content)
        info['enums'] = enums
        
        # 提取类型定义
        types = re.findall(r'export\s+type\s+(\w+)', content)
        info['types'] = types
        
        # 提取函数声明
        functions = re.findall(r'export\s+(?:async\s+)?function\s+(\w+)', content)
        info['functions'] = functions
        
        return info
    
    def generate_doc_entry(self, ts_file: Path, doc_id: str, content: str) -> Dict:
        """为 .d.ts 文件生成文档索引条目"""
        # 提取元信息
        type_info = self.extract_type_definitions(content)
        
        # 生成摘要
        summary = f"TypeScript 类型定义。包含: "
        items = []
        if type_info['interfaces']:
            items.append(f"{len(type_info['interfaces'])} 个接口")
        if type_info['classes']:
            items.append(f"{len(type_info['classes'])} 个类")
        if type_info['functions']:
            items.append(f"{len(type_info['functions'])} 个函数")
        if type_info['types']:
            items.append(f"{len(type_info['types'])} 个类型")
        summary += ", ".join(items) if items else "导出成员"
        
        # 生成关键词
        keywords = []
        keywords.extend(type_info['interfaces'])
        keywords.extend(type_info['classes'])
        keywords.extend(type_info['functions'])
        keywords.append(ts_file.stem)
        
        # 相对路径用于索引
        relative_path = ts_file.relative_to(self.data_dir)
        
        return {
            'id': doc_id,
            'title': f"{ts_file.stem} (TypeScript)",
            'category': 'typescript-definitions',
            'path': str(relative_path),
            'summary': summary,
            'keywords': list(set(keywords))[:15],
            'type_info': type_info,
            'content_length': len(content)
        }
    
    def build_index(self):
        """构建 .d.ts 文件的文档索引"""
        print("发现 .d.ts 文件...")
        dts_files = self.discover_dts_files()
        
        if not dts_files:
            print("未发现任何 .d.ts 文件")
            return {
                'total': 0,
                'documents': []
            }
        
        print(f"发现 {len(dts_files)} 个 .d.ts 文件，开始索引...")
        
        for i, ts_file in enumerate(dts_files):
            try:
                content = ts_file.read_text(encoding='utf-8')
                doc_id = f"dts_{i:04d}"
                
                doc_entry = self.generate_doc_entry(ts_file, doc_id, content)
                self.documents.append(doc_entry)
                
                print(f"  ✓ {ts_file.relative_to(self.data_dir)}")
            
            except Exception as e:
                print(f"  ✗ {ts_file.relative_to(self.data_dir)}: {e}")
        
        return {
            'total': len(self.documents),
            'documents': self.documents
        }
    
    def merge_with_existing_index(self, existing_index_file: Path):
        """将 .d.ts 索引合并到现有的文档索引中"""
        if not existing_index_file.exists():
            print(f"警告: 现有索引不存在: {existing_index_file}")
            return
        
        print(f"合并到现有索引: {existing_index_file}")
        
        with open(existing_index_file, 'r', encoding='utf-8') as f:
            existing_index = json.load(f)
        
        # 将 .d.ts 文档添加到现有索引
        existing_docs = existing_index.get('documents', [])
        
        # 找到最大的 doc_id 编号
        max_id = 0
        for doc in existing_docs:
            if doc['id'].startswith('doc_'):
                try:
                    num = int(doc['id'].split('_')[1])
                    max_id = max(max_id, num)
                except:
                    pass
        
        # 重新编号 .d.ts 文档
        for doc in self.documents:
            max_id += 1
            doc['id'] = f"dts_{max_id:04d}"
        
        # 添加新文档
        existing_docs.extend(self.documents)
        existing_index['documents'] = existing_docs
        
        # 更新分类索引
        if 'categories' not in existing_index:
            existing_index['categories'] = {}
        
        if 'typescript-definitions' not in existing_index['categories']:
            existing_index['categories']['typescript-definitions'] = []
        
        for doc in self.documents:
            if doc['id'] not in existing_index['categories']['typescript-definitions']:
                existing_index['categories']['typescript-definitions'].append(doc['id'])
        
        # 更新总数
        existing_index['total'] = len(existing_docs)
        
        # 保存更新后的索引
        with open(existing_index_file, 'w', encoding='utf-8') as f:
            json.dump(existing_index, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 已将 {len(self.documents)} 个 .d.ts 文档合并到索引中")


def main():
    """主函数"""
    # 获取项目根目录
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    data_dir = project_root / "data"
    index_dir = project_root / "output" / "index"
    
    # 检查必要的目录
    if not data_dir.exists():
        print(f"错误: 数据目录不存在: {data_dir}")
        return 1
    
    if not index_dir.exists():
        print(f"警告: 索引目录不存在: {index_dir}")
        index_dir.mkdir(parents=True, exist_ok=True)
    
    # 构建索引
    indexer = DtsIndexer(str(data_dir), str(index_dir))
    dts_index = indexer.build_index()
    
    if dts_index['total'] > 0:
        # 合并到现有的文档索引
        doc_index_file = index_dir / "doc-index.json"
        indexer.merge_with_existing_index(doc_index_file)
    
    print(f"\n.d.ts 文件索引完成! 共索引 {dts_index['total']} 个文件")
    return 0


if __name__ == "__main__":
    exit(main())
