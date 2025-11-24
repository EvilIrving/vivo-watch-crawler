# BlueOS 文档 MCP 服务器

基于 Model Context Protocol (MCP) 的 vivo BlueOS 手表开发文档服务，为开发者提供智能化的文档查询、代码验证和最佳实践建议。

## 功能特性

- ✅ **快速引用机制**: 通过 `@blueos-api.json` 等标识符快速访问文档资源
- ✅ **文档搜索**: 关键词搜索和语义匹配
- ✅ **代码示例查找**: 快速查找特定功能的代码示例
- ✅ **TypeScript 类型定义支持**: 直接索引 `.d.ts` 文件
- ✅ **双传输模式**: 支持 STDIO 和 SSE/HTTP 两种传输协议
- ✅ **多客户端支持**: 兼容 Claude Desktop、VS Code、Qoder 等

## 目录结构

```
mcp-server/
├── src/                      # MCP 服务器源代码
│   ├── server.py            # 服务器主程序
│   ├── engines/
│   │   ├── ref_resolver.py  # 引用解析器
│   │   └── search_engine.py # 搜索引擎
│   └── ...
├── scripts/                  # 数据构建脚本
│   ├── build_refs.py        # 构建资源引用映射表
│   ├── index_dts_files.py   # 索引 TypeScript 定义文件
│   ├── extract_rules.py     # 提取规则知识库
│   └── start_server.sh      # 启动脚本
├── config/                   # 配置文件
│   ├── server_config.json   # 服务器配置
│   └── mcp_config.json      # MCP 客户端配置示例
├── data/                     # 数据目录
│   ├── resource-refs.json   # 资源引用映射表
│   └── rules-knowledge-base.json  # 规则知识库
├── requirements.txt          # Python 依赖
└── README.md                 # 本文档
```

---

# 📚 使用指南

## 第一部分：环境准备

### 0. 环境要求

- Python 3.8+
- pip
- 网络连接（需访问爬虫生成的文档资源）

### 1. 进入 mcp-server 目录

```bash
cd mcp-server
```

### 2. 创建虚拟环境

#### 方式 A: 使用虚拟环境（推荐）

**macOS/Linux:**
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

**Windows:**
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

#### 方式 B: 不使用虚拟环境（不推荐）

```bash
# 直接使用 pip3 安装依赖
pip3 install -r requirements.txt
```

---

## 第二部分：初始化服务数据

### 步骤 1: 索引 TypeScript 类型定义文件（如果有新的 .d.ts 文件）

```bash
python3 scripts/index_dts_files.py
```

此步骤会：
- 扫描 `../data/api/` 目录
- 提取接口、函数、类型等定义
- 生成可搜索的文档索引

### 步骤 2: 构建资源引用映射表

```bash
python3 scripts/build_refs.py
```

此步骤会生成 `data/resource-refs.json`，包含：
- 所有文档资源的快速引用标识符
- TypeScript 定义文件的引用
- 模式匹配规则

### 步骤 3: 提取规则知识库（可选）

```bash
python3 scripts/extract_rules.py
```

此步骤会生成 `data/rules-knowledge-base.json`，用于代码验证和最佳实践建议。

---

## 第三部分：启动 MCP 服务器

### 选项 A: STDIO 模式（推荐用于 Claude Desktop、VS Code）

```bash
python3 -m src.server --transport stdio
```

该模式通过标准输入输出与客户端通信。

### 选项 B: SSE 模式（推荐用于 Qoder、Web 客户端）

```bash
python3 -m src.server --transport sse --port 8080
```

该模式启动 HTTP 服务器，监听地址为 `http://127.0.0.1:8000`（由 Uvicorn 管理）。

> **注意**：虽然指定了 `--port 8080`，但实际监听端口为 `8000`。

### 选项 C: 使用启动脚本

```bash
bash scripts/start_server.sh
```

---

## 第四部分：客户端集成

### Claude Desktop 集成

1. 编辑配置文件：
   ```
   ~/Library/Application Support/Claude/claude_desktop_config.json
   ```

2. 添加或修改 MCP 服务器配置：
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
         "cwd": "/Users/actor/Documents/learn self/python/vivo-watch-crawler/mcp-server",
         "env": {
           "PYTHONPATH": "/Users/actor/Documents/learn self/python/vivo-watch-crawler/mcp-server"
         }
       }
     }
   }
   ```

3. 重启 Claude Desktop，即可在对话中使用 MCP 工具

### Qoder 集成

1. 先启动 MCP 服务器（SSE 模式）：
   ```bash
   python3 -m src.server --transport sse --port 8080
   ```

2. 编辑配置文件：
   ```
   ~/Library/Application Support/Qoder/SharedClientCache/mcp.json
   ```

3. 添加服务器配置：
   ```json
   {
     "mcpServers": {
       "blueos-docs": {
         "type": "sse",
         "url": "http://127.0.0.1:8000/mcp"
       }
     }
   }
   ```

4. 刷新 Qoder，即可使用 MCP 工具

### VS Code 集成

1. 在 VS Code 设置中配置 MCP 服务器（具体方式取决于使用的 MCP 扩展）

2. 类似 Claude Desktop，使用 STDIO 模式

---

## 第五部分：MCP 工具使用

### 可用工具

#### 1. search_documentation

搜索 BlueOS 开发文档

**参数**：
- `query` (string): 搜索关键词或问题描述
- `category` (string, 可选): 分类过滤 - `js-api`、`ui-component`、`tutorial`、`all`（默认）
- `limit` (int, 可选): 返回结果数量限制（默认 5）

**示例**：
```
搜索 Router API 的使用方法
```

#### 2. get_resource

通过引用标识符获取资源

**参数**：
- `resource_ref` (string): 引用标识符，如 `@blueos-api.json` 或 `@blueos-api/app/appmanager/router.d.ts`
- `format` (string, 可选): 返回格式 - `raw` 或 `formatted`（默认）

**示例**：
```
获取 @blueos-api-complete.md 中的 Battery API 部分
```

#### 3. find_code_examples

查找特定功能的代码示例

**参数**：
- `feature` (string): 功能描述
- `category` (string, 可选): 分类过滤
- `language` (string, 可选): 语言过滤（如 `typescript`、`javascript`）

**示例**：
```
找一个关于列表虚拟滚动的代码示例
```

---

## 第六部分：快速引用标识符

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

### TypeScript 类型定义文件

| 引用格式 | 说明 |
|--------|------|
| `@blueos-api/app/appmanager/router.d.ts` | 路由管理器类型定义 |
| `@blueos-api/hardware/battery/battery.d.ts` | 电池硬件 API 类型定义 |
| `@blueos-api/network/fetch.d.ts` | 网络请求 API 类型定义 |
| `@blueos-api/storage/file.d.ts` | 文件存储 API 类型定义 |

---

## 第七部分：故障排查

### 问题：服务器无法启动

**检查清单**：
1. 检查数据文件是否存在：
   ```bash
   ls data/resource-refs.json
   ```

2. 如果不存在，运行构建脚本：
   ```bash
   python3 scripts/build_refs.py
   python3 scripts/index_dts_files.py
   ```

3. 检查依赖是否安装：
   ```bash
   pip list | grep mcp
   ```

### 问题：Claude Desktop 无法连接

**检查清单**：
1. 确保使用绝对路径（不要使用 `~`）
2. 确保 `cwd` 和 `PYTHONPATH` 正确
3. 重启 Claude Desktop
4. 查看 Claude Desktop 的日志文件（通常在 `~/Library/Logs/Claude`）

### 问题：Qoder 无法连接

**检查清单**：
1. 确保 MCP 服务器已启动（SSE 模式）
2. 检查服务器是否监听在正确的地址：
   ```bash
   curl http://127.0.0.1:8000/mcp
   ```
3. 确保配置中的 URL 是 `http://127.0.0.1:8000/mcp`
4. 刷新或重启 Qoder

### 问题：找不到文档资源

**排查步骤**：
1. 确保爬虫已运行并生成了 `output` 目录：
   ```bash
   cd ../
   ls output/index/
   ls output/llm-ready/combined/
   ```

2. 重新运行构建脚本：
   ```bash
   cd mcp-server
   python3 scripts/build_refs.py
   ```

3. 检查 `data/resource-refs.json` 是否包含预期的资源

### 问题：TypeScript 定义文件未被索引

**排查步骤**：
1. 确保 `.d.ts` 文件在 `../data/api/` 目录下
2. 运行索引脚本：
   ```bash
   python3 scripts/index_dts_files.py
   ```
3. 检查 `../output/index/doc-index.json` 中是否有 `typescript-definitions` 分类
4. 重新运行 `build_refs.py`

---

## 第八部分：开发说明

### 添加新工具

在 `src/server.py` 中添加新的 `@mcp.tool()` 函数：

```python
@mcp.tool()
async def your_tool_name(param1: str, param2: int = 10) -> str:
    """工具描述"""
    # 实现逻辑
    return json.dumps(result)
```

### 添加新资源

在 `src/server.py` 中添加新的 `@mcp.resource()` 函数：

```python
@mcp.resource("blueos://your-resource/{param}")
async def your_resource(param: str) -> str:
    """资源描述"""
    # 实现逻辑
    return content
```

### 修改引用映射

编辑 `scripts/build_refs.py`，在 `build()` 方法中添加新的资源引用。

---

## 常见任务

### 更新爬虫文档后重建索引

```bash
# 在项目根目录运行爬虫
cd ../
./run.sh

# 返回 mcp-server 重建索引
cd mcp-server
python3 scripts/index_dts_files.py
python3 scripts/build_refs.py

# 重启服务器
python3 -m src.server --transport stdio
```

### 添加新的 TypeScript 定义文件

1. 将 `.d.ts` 文件放入 `../data/api/` 目录
2. 运行索引脚本：
   ```bash
   python3 scripts/index_dts_files.py
   ```
3. 重建引用映射：
   ```bash
   python3 scripts/build_refs.py
   ```
4. 重启服务器

### 清空缓存重新初始化

```bash
# 删除生成的数据文件
rm -f data/resource-refs.json
rm -f data/rules-knowledge-base.json

# 重新构建
python3 scripts/index_dts_files.py
python3 scripts/build_refs.py
python3 scripts/extract_rules.py

# 启动服务
python3 -m src.server --transport stdio
```

### 退出虚拟环境

```bash
deactivate
```

### 删除虚拟环境

```bash
rm -rf venv/
```

---

## 许可证

MIT License

## 相关链接

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [vivo BlueOS 开发者文档](https://developers.vivo.com/product/blueos)
- [项目主 README](../README.md)
