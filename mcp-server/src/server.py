"""
BlueOS 文档 MCP 服务器主程序

提供文档查询、代码验证和最佳实践建议功能
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP 服务器
mcp = FastMCP("blueos-docs")

# 配置文件路径
CONFIG_DIR = Path(__file__).parent.parent / "config"
DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "output"


def load_config() -> Dict[str, Any]:
    """加载服务器配置"""
    config_file = CONFIG_DIR / "server_config.json"
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


# 加载配置
config = load_config()


@mcp.tool()
async def search_documentation(
    query: str,
    category: str = "all",
    limit: int = 5
) -> str:
    """搜索 BlueOS 开发文档与 API 类型定义
    
    支持搜索 JavaScript API 文档、UI 组件、开发教程以及 TypeScript 类型定义文件。
    
    Args:
        query: 搜索关键词或问题描述。支持以下查询方式:
            - API 查询: "database", "network", "bluetooth" 等
            - 类型查询: "interface", "接口", "function", "函数" 等
            - 特定元素: "EventManager", "BatteryManager" 等
        category: 文档分类 (js-api/ui-component/tutorial/typescript-definitions/all)
        limit: 返回结果数量限制
    
    Returns:
        匹配的文档列表(JSON格式)。对于 TypeScript 查询会优先返回 .d.ts 类型定义文件
    """
    try:
        from src.engines.search_engine import SearchEngine
        
        doc_index = OUTPUT_DIR / "index" / "doc-index.json"
        engine = SearchEngine(str(doc_index))
        
        results = engine.search(query, category, limit)
        
        return json.dumps({
            "success": True,
            "results": results,
            "total": len(results)
        }, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        }, ensure_ascii=False)


@mcp.tool()
async def get_resource(
    resource_ref: str,
    format: str = "formatted"
) -> str:
    """通过引用标识符获取资源
    
    Args:
        resource_ref: 资源引用标识符 (如 @blueos-api.json)
        format: 返回格式 (raw/formatted)
    
    Returns:
        资源内容和元数据
    """
    try:
        from src.engines.ref_resolver import RefResolver
        
        refs_file = DATA_DIR / "resource-refs.json"
        resolver = RefResolver(str(refs_file), str(OUTPUT_DIR.parent))
        
        ref_info = resolver.resolve(resource_ref)
        
        if not ref_info:
            return json.dumps({
                "success": False,
                "error": f"资源未找到: {resource_ref}"
            }, ensure_ascii=False)
        
        # 读取文件内容
        file_path = Path(ref_info['absolute_path'])
        content = file_path.read_text(encoding='utf-8')
        
        return json.dumps({
            "success": True,
            "ref": resource_ref,
            "mime_type": ref_info['type'],
            "content": content,
            "metadata": {
                "description": ref_info.get('description', ''),
                "category": ref_info.get('category', ''),
                "size": ref_info.get('size', 0)
            }
        }, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        }, ensure_ascii=False)


@mcp.tool()
async def find_code_examples(
    feature: str,
    category: str = None,
    language: str = None
) -> str:
    """查找特定功能的代码示例
    
    Args:
        feature: 功能描述
        category: 示例分类过滤 (可选)
        language: 编程语言过滤 (可选)
    
    Returns:
        代码示例列表
    """
    try:
        examples_file = OUTPUT_DIR / "index" / "code-examples-index.json"
        
        with open(examples_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_examples = data.get('examples', [])
        
        # 简单的关键词匹配
        feature_lower = feature.lower()
        matched = []
        
        for example in all_examples:
            # 匹配源标题或代码内容
            source_title = example.get('source_title', '').lower()
            code = example.get('code', '').lower()
            
            if feature_lower in source_title or feature_lower in code:
                # 分类过滤
                if category and example.get('category') != category:
                    continue
                
                # 语言过滤
                if language and example.get('language') != language:
                    continue
                
                matched.append({
                    "id": example.get('id'),
                    "code": example.get('code'),
                    "language": example.get('language'),
                    "description": example.get('description', ''),
                    "source_title": example.get('source_title'),
                    "source_url": example.get('source_url'),
                    "category": example.get('category')
                })
        
        # 处理 .d.ts 类型定义文件作为代码示例
        if not matched:
            from src.engines.ref_resolver import RefResolver
            
            refs_file = DATA_DIR / "resource-refs.json"
            resolver = RefResolver(str(refs_file), str(OUTPUT_DIR.parent))
            
            # 输记参数，查找匹配的 .d.ts 文件
            dts_pattern = f"@blueos-api/**/{feature_lower}"
            
            data_dir = OUTPUT_DIR.parent / "data" / "api"
            if data_dir.exists():
                for ts_file in data_dir.rglob(f"*{feature_lower}*.d.ts"):
                    try:
                        content = ts_file.read_text(encoding='utf-8')
                        matched.append({
                            "id": f"dts_{ts_file.stem}",
                            "code": content,
                            "language": "typescript",
                            "description": f"TypeScript 类型定义: {ts_file.stem}",
                            "source_title": f"{ts_file.parent.name}/{ts_file.stem}",
                            "source_url": f"@blueos-api/{'/'.join(ts_file.relative_to(data_dir).parts)}",
                            "category": "typescript-definitions"
                        })
                    except Exception:
                        pass
        
        return json.dumps({
            "success": True,
            "examples": matched[:10],  # 限制返回数量
            "total": len(matched),
            "source_ref": "@blueos-examples.json"
        }, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        }, ensure_ascii=False)


@mcp.resource("blueos://ref/{ref}")
async def get_ref_resource(ref: str) -> str:
    """通过引用标识符访问资源"""
    return await get_resource(ref, "raw")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="BlueOS 文档 MCP 服务器")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="传输模式"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="HTTP端口 (仅SSE模式)"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="HTTP主机 (仅SSE模式)"
    )
    
    args = parser.parse_args()
    
    # 检查必要的数据文件
    refs_file = DATA_DIR / "resource-refs.json"
    if not refs_file.exists():
        print("错误: 资源引用映射表不存在，请先运行 scripts/build_refs.py", file=sys.stderr)
        sys.exit(1)
    
    # 启动服务器
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        # SSE 模式
        print(f"启动 SSE 服务器: {args.host}:{args.port}", file=sys.stderr)
        print(f"访问地址: http://{args.host}:{args.port}/sse", file=sys.stderr)
        
        # 设置环境变量让 FastMCP 使用指定的 host 和 port
        import os
        os.environ['MCP_HOST'] = args.host
        os.environ['MCP_PORT'] = str(args.port)
        
        # FastMCP 的 SSE 模式
        mcp.run(transport="sse")


if __name__ == "__main__":
    main()
