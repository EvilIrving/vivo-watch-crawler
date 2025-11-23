# BlueOS 文档 MCP 服务器

基于 Model Context Protocol (MCP) 的 vivo BlueOS 手表开发文档服务，为开发者提供智能化的文档查询、代码验证和最佳实践建议。

## 功能特性

- ✅ **快速引用机制**: 通过 `@blueos-api.json` 等标识符快速访问文档资源
- ✅ **文档搜索**: 关键词搜索和语义匹配
- ✅ **代码示例查找**: 快速查找特定功能的代码示例
- ✅ **双传输模式**: 支持 STDIO 和 SSE/HTTP 两种传输协议
- ✅ **多客户端支持**: 兼容 Claude Desktop、VS Code、Qoder 等

## 快速开始

### 1. 环境准备

```bash
cd mcp-server

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境 (macOS/Linux)
source venv/bin/activate

# 激活虚拟环境 (Windows)
# venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 构建数据文件

```bash
# 构建资源引用映射表
python scripts/build_refs.py

# 提取规则知识库
python scripts/extract_rules.py
```

### 3. 启动服务

**STDIO 模式** (用于 Claude Desktop、VS Code):

```bash
python -m src.server --transport stdio
```

**SSE 模式** (用于 Qoder、Web 客户端):

```bash
python -m src.server --transport sse --port 8080
```

## 客户端集成

### Claude Desktop

编辑配置文件: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "blueos-docs": {
      "command": "python3",
      "args": [
        "-m",
        "src.server",
        "--transport",
        "stdio"
      ],
      "cwd": "/absolute/path/to/vivo-watch-crawler/mcp-server",
      "env": {
        "PYTHONPATH": "/absolute/path/to/vivo-watch-crawler/mcp-server"
      }
    }
  }
}
```

重启 Claude Desktop 后即可使用。

### Qoder

编辑配置文件: `~/Library/Application Support/Qoder/SharedClientCache/mcp.json`

```json
{
  "mcpServers": {
    "blueos-docs": {
      "type": "sse",
      "url": "http://127.0.0.1:8080/mcp"
    }
  }
}
```

先启动 MCP 服务器，然后在 Qoder 中即可使用。

## 使用示例

### 查看 API 索引

```
请展示 @blueos-api.json 中所有 system 相关的 API
```

### 查找代码示例

```
如何实现列表滚动到指定位置？
```

### 获取完整文档

```
根据 @blueos-component-complete.md 中的说明，
list 组件应该如何配置 fisheye 布局？
```

## 可用工具

### search_documentation

搜索 BlueOS 开发文档

**参数**:
- `query`: 搜索关键词
- `category`: 分类过滤 (js-api/ui-component/tutorial/all)
- `limit`: 结果数量限制

### get_resource

通过引用标识符获取资源

**参数**:
- `resource_ref`: 引用标识符 (如 `@blueos-api.json`)
- `format`: 返回格式 (raw/formatted)

### find_code_examples

查找代码示例

**参数**:
- `feature`: 功能描述
- `category`: 分类过滤 (可选)
- `language`: 语言过滤 (可选)

## 快速引用标识符

### 索引类资源

| 标识符 | 说明 |
|--------|------|
| `@blueos-api.json` | JavaScript API 索引 |
| `@blueos-component.json` | UI 组件索引 |
| `@blueos-doc.json` | 文档总索引 |
| `@blueos-examples.json` | 代码示例索引 |

### 完整文档资源

| 标识符 | 说明 |
|--------|------|
| `@blueos-api-complete.md` | JavaScript API 完整文档 |
| `@blueos-component-complete.md` | UI 组件完整文档 |
| `@blueos-tutorial-complete.md` | 开发教程完整文档 |

### 规则和规范资源

| 标识符 | 说明 |
|--------|------|
| `@blueos-component-rules.md` | 组件使用规范 |
| `@blueos-api-rules.md` | API 调用规范 |
| `@blueos-perf-guide.md` | 性能优化指南 |

## 目录结构

```
mcp-server/
├── src/
│   ├── server.py              # MCP 服务器主程序
│   ├── engines/
│   │   ├── ref_resolver.py    # 引用解析器
│   │   └── search_engine.py   # 搜索引擎
│   └── ...
├── data/
│   ├── resource-refs.json     # 资源引用映射表
│   └── rules-knowledge-base.json  # 规则知识库
├── config/
│   ├── server_config.json     # 服务配置
│   └── mcp_config.json        # 客户端配置示例
├── scripts/
│   ├── build_refs.py          # 构建引用映射表
│   └── extract_rules.py       # 提取规则知识库
├── requirements.txt           # Python 依赖
└── README.md                  # 本文档
```

## 故障排查

### 服务器无法启动

1. 检查是否已构建数据文件:
   ```bash
   ls data/resource-refs.json
   ```

2. 如果不存在，运行构建脚本:
   ```bash
   python scripts/build_refs.py
   python scripts/extract_rules.py
   ```

### Claude Desktop 无法连接

1. 检查配置文件路径是否正确
2. 确保使用绝对路径
3. 重启 Claude Desktop
4. 查看 Claude Desktop 的日志文件

### 找不到文档

确保爬虫已运行并生成了 `output` 目录:

```bash
cd ../
ls output/index/
ls output/llm-ready/combined/
```

## 开发说明

### 添加新工具

在 `src/server.py` 中添加新的 `@mcp.tool()` 函数:

```python
@mcp.tool()
async def your_tool_name(param1: str, param2: int = 10) -> str:
    """工具描述"""
    # 实现逻辑
    return json.dumps(result)
```

### 添加新资源

在 `src/server.py` 中添加新的 `@mcp.resource()` 函数:

```python
@mcp.resource("blueos://your-resource/{param}")
async def your_resource(param: str) -> str:
    """资源描述"""
    # 实现逻辑
    return content
```

## 许可证

MIT License

## 相关链接

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [vivo BlueOS 开发者文档](https://developers.vivo.com/product/blueos)
