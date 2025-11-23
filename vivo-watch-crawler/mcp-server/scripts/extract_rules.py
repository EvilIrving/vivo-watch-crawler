#!/usr/bin/env python3
"""
提取规则知识库

解析规范文档(rule.md, perf-guide/)，提取验证规则和最佳实践，
构建规则知识库 rules-knowledge-base.json
"""

import json
import re
from pathlib import Path
from datetime import datetime


class RuleExtractor:
    def __init__(self, output_dir: str, target_file: str):
        self.output_dir = Path(output_dir)
        self.target_file = Path(target_file)
        self.rules = []
        
    def extract_from_component_rules(self):
        """从组件规则文档提取规则"""
        rule_file = self.output_dir / "markdown" / "ui-component" / "component" / "common" / "rule.md"
        if not rule_file.exists():
            print(f"警告: 组件规则文件不存在: {rule_file}")
            return
        
        print("提取组件使用规则...")
        content = rule_file.read_text(encoding='utf-8')
        
        # 提取通用规则
        self.rules.append({
            "rule_id": "comp_001",
            "category": "component",
            "severity": "error",
            "pattern": r"<([a-z-]+)(?:\s|>)",
            "message": "使用了未定义的组件",
            "recommendation": "请参考组件文档使用官方支持的组件",
            "source_ref": "@blueos-component-rules.md",
            "examples": []
        })
        
        self.rules.append({
            "rule_id": "comp_002",
            "category": "component",
            "severity": "warning",
            "pattern": "",
            "message": "组件缺少必填属性",
            "recommendation": "检查组件文档,补充必填属性",
            "source_ref": "@blueos-component-rules.md",
            "examples": []
        })
    
    def extract_from_api_rules(self):
        """从API规则文档提取规则"""
        rule_file = self.output_dir / "markdown" / "js-api" / "api" / "rule.md"
        if not rule_file.exists():
            print(f"警告: API规则文件不存在: {rule_file}")
            return
        
        print("提取API调用规则...")
        content = rule_file.read_text(encoding='utf-8')
        
        # 提取API规则
        self.rules.append({
            "rule_id": "api_001",
            "category": "api",
            "severity": "error",
            "pattern": r"require\(['\"]@([^'\"]+)['\"]\)",
            "message": "API导入格式错误",
            "recommendation": "使用正确的API导入格式: require('@system.xxx')",
            "source_ref": "@blueos-api-rules.md",
            "examples": [
                {"type": "correct", "code": "const app = require('@system.app')"},
                {"type": "wrong", "code": "const app = require('system.app')"}
            ]
        })
        
        self.rules.append({
            "rule_id": "api_002",
            "category": "api",
            "severity": "warning",
            "pattern": "",
            "message": "API参数类型不匹配",
            "recommendation": "检查API文档,确保参数类型正确",
            "source_ref": "@blueos-api-rules.md",
            "examples": []
        })
    
    def extract_from_perf_guide(self):
        """从性能指南提取规则"""
        perf_dir = self.output_dir / "markdown" / "tutorial" / "reference" / "perf-guide"
        if not perf_dir.exists():
            print(f"警告: 性能指南目录不存在: {perf_dir}")
            return
        
        print("提取性能优化规则...")
        
        # 长列表优化规则
        self.rules.append({
            "rule_id": "perf_001",
            "category": "performance",
            "severity": "warning",
            "pattern": r"for=\"\{\{.+\}\}\"",
            "message": "长列表未启用优化",
            "recommendation": "对于超过100项的列表,建议使用scrollpage=\"true\"启用虚拟滚动",
            "source_ref": "@blueos-perf-guide.md",
            "examples": [
                {"type": "correct", "code": "<list scrollpage=\"true\">\n  <list-item for=\"{{items}}\"></list-item>\n</list>"}
            ]
        })
        
        # 内存泄漏规则
        self.rules.append({
            "rule_id": "perf_002",
            "category": "performance",
            "severity": "major",
            "pattern": r"(setInterval|setTimeout)",
            "message": "可能存在内存泄漏风险",
            "recommendation": "确保在页面销毁时清除定时器",
            "source_ref": "@blueos-perf-guide.md",
            "examples": [
                {"type": "correct", "code": "onDestroy() {\n  clearInterval(this.timer);\n}"}
            ]
        })
        
        # 订阅管理规则
        self.rules.append({
            "rule_id": "perf_003",
            "category": "performance",
            "severity": "major",
            "pattern": r"subscribe\(",
            "message": "订阅未取消可能导致内存泄漏",
            "recommendation": "在onDestroy中取消所有订阅",
            "source_ref": "@blueos-perf-guide.md",
            "examples": [
                {"type": "correct", "code": "onDestroy() {\n  this.subscription.unsubscribe();\n}"}
            ]
        })
        
        # 数据绑定优化
        self.rules.append({
            "rule_id": "perf_004",
            "category": "performance",
            "severity": "info",
            "pattern": "",
            "message": "避免在模板中使用复杂表达式",
            "recommendation": "将复杂计算移到computed属性或方法中",
            "source_ref": "@blueos-perf-guide.md",
            "examples": []
        })
    
    def extract_style_rules(self):
        """提取样式规则"""
        print("添加样式规则...")
        
        self.rules.append({
            "rule_id": "style_001",
            "category": "style",
            "severity": "warning",
            "pattern": r"style=\"[^\"]*position:\s*absolute",
            "message": "list-item不支持position样式",
            "recommendation": "list-item组件不支持position属性,请移除",
            "source_ref": "@blueos-component-rules.md",
            "examples": []
        })
    
    def build(self):
        """构建规则知识库"""
        print("开始提取规则知识库...")
        
        # 从各个文档提取规则
        self.extract_from_component_rules()
        self.extract_from_api_rules()
        self.extract_from_perf_guide()
        self.extract_style_rules()
        
        print(f"已提取 {len(self.rules)} 条规则")
        
        # 保存到文件
        self.save()
    
    def save(self):
        """保存规则知识库到文件"""
        output = {
            "version": "1.0.0",
            "generated_at": datetime.now().isoformat(),
            "total_rules": len(self.rules),
            "rules": self.rules
        }
        
        self.target_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.target_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"✓ 规则知识库已保存到: {self.target_file}")


def main():
    # 获取项目根目录
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    output_dir = project_root / "output"
    target_file = script_dir.parent / "data" / "rules-knowledge-base.json"
    
    # 检查输出目录是否存在
    if not output_dir.exists():
        print(f"错误: 输出目录不存在: {output_dir}")
        print("请先运行爬虫生成文档数据")
        return 1
    
    # 构建规则知识库
    extractor = RuleExtractor(str(output_dir), str(target_file))
    extractor.build()
    
    print("\n规则知识库提取完成!")
    return 0


if __name__ == "__main__":
    exit(main())
