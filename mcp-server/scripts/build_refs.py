#!/usr/bin/env python3
"""
构建资源引用映射表

扫描 output 目录下的所有文档和索引文件,为每个资源生成快速引用标识符,
构建引用映射表 resource-refs.json
"""

import json
import os
import hashlib
from pathlib import Path
from datetime import datetime


class RefBuilder:
    def __init__(self, output_dir: str, target_file: str):
        self.output_dir = Path(output_dir)
        self.target_file = Path(target_file)
        self.refs = {}
        self.patterns = []
        
    def calculate_checksum(self, file_path: Path) -> str:
        """计算文件SHA256校验和"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return f"sha256:{sha256.hexdigest()}"
    
    def get_file_size(self, file_path: Path) -> int:
        """获取文件大小"""
        return file_path.stat().st_size
    
    def get_mime_type(self, file_path: Path) -> str:
        """根据文件扩展名返回MIME类型"""
        ext = file_path.suffix.lower()
        mime_types = {
            '.json': 'application/json',
            '.md': 'text/markdown',
            '.txt': 'text/plain',
            '.d.ts': 'application/typescript',
            '.ts': 'application/typescript'
        }
        return mime_types.get(ext, 'application/octet-stream')
    
    def add_static_ref(self, ref: str, file_path: Path, description: str, category: str):
        """添加静态引用"""
        relative_path = file_path.relative_to(self.output_dir.parent.parent)
        
        self.refs[ref] = {
            "path": str(relative_path),
            "type": self.get_mime_type(file_path),
            "description": description,
            "category": category,
            "size": self.get_file_size(file_path),
            "checksum": self.calculate_checksum(file_path)
        }
    
    def add_pattern(self, pattern: str, template: str, description: str):
        """添加模式匹配规则"""
        self.patterns.append({
            "pattern": pattern,
            "template": template,
            "description": description
        })
    
    def _generate_dts_ref(self, ts_file: Path, base_dir: Path) -> str:
        """为 .d.ts 文件生成引用标识符"""
        relative = ts_file.relative_to(base_dir)
        # 将路径转换为引用: app/appmanager/router.d.ts -> @blueos-api/app/appmanager/router.d.ts
        parts = relative.parts
        ref_path = '/'.join(parts)
        return f"@blueos-api/{ref_path}"
    
    def build(self):
        """构建引用映射表"""
        print("开始构建资源引用映射表...")
        
        # 索引类资源
        index_dir = self.output_dir / "index"
        if index_dir.exists():
            for index_file in index_dir.glob("*.json"):
                name = index_file.stem
                if name == "api-index":
                    self.add_static_ref(
                        "@blueos-api.json",
                        index_file,
                        "JavaScript API 索引",
                        "index"
                    )
                elif name == "component-index":
                    self.add_static_ref(
                        "@blueos-component.json",
                        index_file,
                        "UI 组件索引",
                        "index"
                    )
                elif name == "doc-index":
                    self.add_static_ref(
                        "@blueos-doc.json",
                        index_file,
                        "文档总索引",
                        "index"
                    )
                elif name == "code-examples-index":
                    self.add_static_ref(
                        "@blueos-examples.json",
                        index_file,
                        "代码示例索引",
                        "index"
                    )
        
        # 完整文档资源
        combined_dir = self.output_dir / "llm-ready" / "combined"
        if combined_dir.exists():
            for combined_file in combined_dir.glob("*.md"):
                name = combined_file.stem
                if name == "js-api-complete":
                    self.add_static_ref(
                        "@blueos-api-complete.md",
                        combined_file,
                        "JavaScript API 完整文档",
                        "combined"
                    )
                elif name == "ui-component-complete":
                    self.add_static_ref(
                        "@blueos-component-complete.md",
                        combined_file,
                        "UI 组件完整文档",
                        "combined"
                    )
                elif name == "tutorial-complete":
                    self.add_static_ref(
                        "@blueos-tutorial-complete.md",
                        combined_file,
                        "开发教程完整文档",
                        "combined"
                    )
        
        # 规则和规范资源
        # 组件规则
        component_rule = self.output_dir / "markdown" / "ui-component" / "component" / "common" / "rule.md"
        if component_rule.exists():
            self.add_static_ref(
                "@blueos-component-rules.md",
                component_rule,
                "组件使用规范",
                "rules"
            )
        
        # API 规则
        api_rule = self.output_dir / "markdown" / "js-api" / "api" / "rule.md"
        if api_rule.exists():
            self.add_static_ref(
                "@blueos-api-rules.md",
                api_rule,
                "API 调用规范",
                "rules"
            )
        
        # 性能指南 (需要合并多个文件,这里先指向第一个)
        perf_guide_dir = self.output_dir / "markdown" / "tutorial" / "reference" / "perf-guide"
        if perf_guide_dir.exists() and (perf_guide_dir / "overview.md").exists():
            self.add_static_ref(
                "@blueos-perf-guide.md",
                perf_guide_dir / "overview.md",
                "性能优化指南",
                "rules"
            )
        
        # 索引 .d.ts 类型定义文件
        data_dir = self.output_dir.parent / "data" / "api"
        if data_dir.exists():
            for ts_file in data_dir.rglob("*.d.ts"):
                # 生成引用标识符: @blueos-api/{category}/{name}.d.ts
                relative_path = ts_file.relative_to(data_dir.parent)
                ref_name = self._generate_dts_ref(ts_file, data_dir)
                
                if ref_name:
                    self.add_static_ref(
                        ref_name,
                        ts_file,
                        f"TypeScript 类型定义: {ts_file.stem}",
                        "typescript-definitions"
                    )
        
        # 添加模式匹配规则
        # API 命名空间文档
        self.add_pattern(
            r"@blueos-api/([a-z-]+)\.md",
            "output/markdown/js-api/api/{0}.md",
            "API 命名空间文档"
        )
        
        # UI 组件文档
        self.add_pattern(
            r"@blueos-component/([a-z-]+)\.md",
            "output/markdown/ui-component/component/**/{0}.md",
            "UI 组件文档"
        )
        
        # TypeScript 类型定义文件模式
        self.add_pattern(
            r"@blueos-api/(.+)\.d\.ts",
            "data/api/{0}.d.ts",
            "TypeScript 类型定义"
        )
        
        print(f"已生成 {len(self.refs)} 个静态引用")
        print(f"已添加 {len(self.patterns)} 个模式匹配规则")
        
        # 保存到文件
        self.save()
    
    def save(self):
        """保存映射表到文件"""
        output = {
            "version": "1.0.0",
            "generated_at": datetime.now().isoformat(),
            "refs": self.refs,
            "patterns": self.patterns
        }
        
        self.target_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.target_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"✓ 映射表已保存到: {self.target_file}")


def main():
    # 获取项目根目录
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    output_dir = project_root / "output"
    target_file = script_dir.parent / "data" / "resource-refs.json"
    
    # 检查输出目录是否存在
    if not output_dir.exists():
        print(f"错误: 输出目录不存在: {output_dir}")
        print("请先运行爬虫生成文档数据")
        return 1
    
    # 构建引用映射表
    builder = RefBuilder(str(output_dir), str(target_file))
    builder.build()
    
    print("\n资源引用映射表构建完成!")
    return 0


if __name__ == "__main__":
    exit(main())
