# vivo 手表文档爬虫使用指南

## 项目概述

本项目用于自动爬取 vivo BlueOS 手表开发文档，并转换为适合大语言模型（LLM）使用的 Markdown 格式文档。采用高效的 HTML API 爬取策略，直接获取页面内容，无需浏览器自动化工具。

### 核心功能

- 🚀 **HTML API 爬取**：直接访问 HTML 页面（`?hastopwindow=1`），速度快、稳定性高
- 🔍 **自动发现**：从导航页面自动提取所有文档链接（161 个页面）
- 📑 **智能分类**：自动识别教程(tutorial)、JS API、UI 组件三大类别
- 🔍 **内容提取**：精准提取标题、正文、代码示例及元数据
- 📝 **格式转换**：HTML 转 Markdown，保持代码示例格式
- 🤖 **LLM 优化**：生成合并文档和问答对数据集
- 📊 **索引构建**：为文档搜索和 MCP 服务提供索引支持

## 快速开始

### 0. 环境要求

- **Python 版本**: 3.8 或更高
- **操作系统**: macOS / Linux / Windows
- **网络**: 需要能访问 `developers-watch.vivo.com.cn`
- **存储空间**: 至少 100MB （存储文档和索引）

### 1. 创建虚拟环境（强烈推荐）

虚拟环境可以隔离项目依赖，避免与系统 Python 包冲突。

**macOS / Linux:**
```bash
cd vivo-watch-crawler

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 验证激活成功（命令行前缀显示 (venv)）
which python
# 输出应为: /path/to/vivo-watch-crawler/venv/bin/python
```

**Windows:**
```bash
cd vivo-watch-crawler

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 验证激活成功（命令行前缀显示 (venv)）
where python
# 输出应为: C:\path\to\vivo-watch-crawler\venv\Scripts\python.exe
```

> **提示**: 激活虚拟环境后，命令行前缀会显示 `(venv)`，表示当前在虚拟环境中。

### 2. 安装依赖

在激活虚拟环境后，安装项目所需的 Python 包：

```bash
# 升级 pip（可选）
pip install --upgrade pip

# 安装依赖
pip install -r requirements.txt
```

**依赖包说明:**
- `requests` - HTTP 请求库
- `beautifulsoup4` - HTML 解析
- `lxml` - XML/HTML 解析器
- `markdownify` - HTML 转 Markdown

> **重要**: 本项目使用 **HTML API 爬取模式**，**不需要** 安装 Playwright 或浏览器驱动！

### 2. 一键运行（推荐）

确保已激活虚拟环境（命令行前缀有 `(venv)`），然后运行：

```bash
chmod +x run.sh
./run.sh
```

**执行流程：**
1. 自动检查 Python 环境和依赖
2. 从导航页面自动发现所有文档链接（161 个）
3. 通过 HTML API 批量爬取页面数据
4. 转换 HTML 为 Markdown 格式
5. 生成 LLM 就绪的合并文档
6. 构建多维度索引文件

**预计用时：** 约 3-8 分钟（取决于网络速度）

**输出示例：**
```
============================================================
开始爬取 vivo 手表文档 (API 模式)
============================================================

阶段一: 发现所有页面
============================================================
从导航页面自动发现所有文档链接...
从导航发现 161 个页面

阶段二: 爬取所有页面
============================================================
[1/161] 处理: /api/ai/nlp/
  ✓ 成功: 自然语言处理
...
```

### 3. 分步运行

**场景：** 当需要单独调试爬虫或转换器时

**步骤 1: 运行爬虫（API 模式）**
```bash
python -m src.crawler.main
```
输出：
- `data/raw/*.jsonl` - 原始爬取数据（JSON Lines 格式）
- `data/metadata/statistics.json` - 爬取统计信息
- `crawler.log` - 详细日志

**步骤 2: 转换和生成**
```bash
python -m src.converter.main
```
输出：
- `output/markdown/` - 分类 Markdown 文档
- `output/llm-ready/` - LLM 优化文档
- `output/index/` - 索引文件
- `converter.log` - 转换日志

## 虚拟环境管理

### 退出虚拟环境

当你完成工作后，可以退出虚拟环境：

```bash
deactivate
```

退出后，命令行前缀的 `(venv)` 会消失。

### 重新激活虚拟环境

下次使用时，只需重新激活：

**macOS / Linux:**
```bash
cd vivo-watch-crawler
source venv/bin/activate
```

**Windows:**
```bash
cd vivo-watch-crawler
venv\Scripts\activate
```

### 删除虚拟环境

如果需要完全删除虚拟环境（例如重新安装依赖）：

**macOS / Linux:**
```bash
# 退出虚拟环境（如果已激活）
deactivate

# 删除虚拟环境目录
rm -rf venv/

# 重新创建（如需）
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```bash
# 退出虚拟环境（如果已激活）
deactivate

# 删除虚拟环境目录
rmdir /s venv

# 重新创建（如需）
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 清理项目数据

**清理爬取数据（重新爬取）:**
```bash
rm -rf data/ output/
```

**完全清理（包括虚拟环境、数据和日志）:**
```bash
rm -rf venv/ data/ output/ *.log
```

> **注意**: 删除 `data/` 后，下次运行会重新爬取所有页面。

## 配置说明

编辑 `config.json` 文件可以自定义配置：

```json
{
  "entry_urls": [
    "https://developers.vivo.com/product/blueos/doc/common/reference/quickstart/introduction",
    "https://developers.vivo.com/product/blueos/doc/common/js/system/app",
    "https://developers.vivo.com/product/blueos/doc/common/component/common/rule"
  ],
  "categories": {                   // 分类规则
    "tutorial": "reference",
    "js-api": "js",
    "ui-component": "component"
  },
  "base_url": "https://developers.vivo.com/product/blueos/doc/",
  "max_workers": 3,                 // 并发数（API 模式暂未使用）
  "retry_times": 3,                 // 失败重试次数
  "delay_range": [1, 3],            // 请求延迟范围（秒）
  "timeout": 30,                    // 超时时间（秒）
  "headless": true,                 // 已废弃（API 模式不需要）
  "user_agent": "...",              // HTTP 请求 User-Agent
  "data_dir": "data",               // 数据存储目录
  "output_dir": "output"            // 输出目录
}
```

### 配置项详解

- **entry_urls**：入口页面 URL 列表，爬虫会从这些页面开始发现所有文档
- **categories**：URL 路径到分类的映射规则
- **delay_range**：每次请求之间的随机延迟，避免请求过快
- **timeout**：单个请求的超时时间

## 输出结构

### 数据目录 (data/)

```
data/
├── raw/                              # 原始爬取数据（JSON Lines 格式）
│   ├── tutorial.jsonl                # 教程类文档
│   ├── js-api.jsonl                  # JavaScript API 文档
│   └── ui-component.jsonl            # UI 组件文档
├── navigation/                       # 导航结构（暂未使用）
│   └── site-structure.json
└── metadata/                         # 元数据
    └── statistics.json               # 爬取统计：总数、成功、失败、跳过
```

**JSONL 格式说明：** 每行一个 JSON 对象，包含 URL、分类、标题、内容、代码示例等

### 输出目录 (output/)

```
output/
├── markdown/                         # Markdown 文档（按分类组织）
│   ├── tutorial/                     # 教程文档
│   │   └── reference/quickstart/
│   │       └── introduction.md
│   ├── js-api/                       # JavaScript API 文档
│   │   └── js/system/
│   │       └── app.md
│   └── ui-component/                 # UI 组件文档
│       └── component/common/
│           └── rule.md
│
├── llm-ready/                        # LLM 优化文档
│   ├── combined/                     # 合并的大文档（适合上下文注入）
│   │   ├── tutorial-complete.md      # 所有教程合并
│   │   ├── js-api-complete.md        # 所有 API 合并
│   │   └── ui-component-complete.md  # 所有组件合并
│   └── qa-pairs/                     # 问答对数据集（适合微调）
│       └── qa-dataset.jsonl          # 问答对 JSON Lines
│
└── index/                            # 索引文件（为 MCP 服务准备）
    ├── doc-index.json                # 文档索引：标题、URL、分类
    ├── api-index.json                # API 索引：名称、命名空间、参数
    ├── component-index.json          # 组件索引：组件名、属性
    └── code-examples-index.json      # 代码示例索引：语言、代码
```

## 使用场景

### 1. LLM 知识库和上下文注入

**文件：** `output/llm-ready/combined/*.md`

**用途：**
- ✅ **RAG 系统**：将文档切片后存入向量数据库，实现语义检索
- ✅ **上下文注入**：直接提供给大模型作为参考文档（如 Claude Projects）
- ✅ **AI 助手**：为开发助手提供 vivo 手表开发知识
- ✅ **模型微调**：作为微调数据集的基础素材

**示例：**
```python
# 使用 LangChain 构建 RAG
from langchain.document_loaders import TextLoader
from langchain.text_splitter import MarkdownTextSplitter

loader = TextLoader('output/llm-ready/combined/js-api-complete.md')
docs = loader.load()
splitter = MarkdownTextSplitter(chunk_size=1000)
chunks = splitter.split_documents(docs)
```

### 2. 代码示例检索

**文件：** `output/index/code-examples-index.json`

**用途：**
- ✅ **IDE 插件**：在编辑器中快速查找代码示例
- ✅ **代码生成**：根据示例生成新代码
- ✅ **学习参考**：提供即时的代码参考

**数据格式：**
```json
{
  "total": 10,
  "examples": [
    {
      "code": "const app = require('@system.app');\napp.getInfo({...});",
      "language": "javascript",
      "source_url": "...",
      "category": "js-api"
    }
  ]
}
```

### 3. 文档搜索和导航

**文件：** `output/index/doc-index.json`、`api-index.json`、`component-index.json`

**用途：**
- ✅ **全文搜索**：构建文档搜索引擎
- ✅ **API 查找**：快速定位 API 文档
- ✅ **组件查询**：查找 UI 组件使用方法
- ✅ **MCP 服务**：为 Model Context Protocol 提供数据支持

**示例：**
```python
import json

# 查找特定 API
with open('output/index/api-index.json') as f:
    api_index = json.load(f)
    
for api in api_index['apis']:
    if 'app' in api['name']:
        print(f"API: {api['name']}, URL: {api['url']}")
```

### 4. 问答系统训练

**文件：** `output/llm-ready/qa-pairs/qa-dataset.jsonl`

**用途：**
- ✅ **微调数据集**：训练专门的问答模型
- ✅ **聊天机器人**：构建技术支持机器人
- ✅ **FAQ 系统**：自动生成常见问题解答

**数据格式：**
```json
{"question": "如何使用 app.getInfo API？", "answer": "...详细说明..."}
{"question": "什么是 BlueOS？", "answer": "...详细说明..."}
```

## 常见问题

### Q: 为什么推荐使用虚拟环境？

**A:** 虚拟环境有以下优点：

1. **隔离依赖** - 避免与系统 Python 包冲突
2. **版本管理** - 不同项目可使用不同版本的包
3. **易于清理** - 删除 `venv/` 目录即可完全清除
4. **部署一致** - 确保开发和生产环境一致

### Q: 如何检查是否在虚拟环境中？

**A:** 查看命令行前缀是否有 `(venv)`，或运行：

```bash
# macOS / Linux
which python
# 应该显示: /path/to/vivo-watch-crawler/venv/bin/python

# Windows
where python
# 应该显示: C:\path\to\vivo-watch-crawler\venv\Scripts\python.exe
```

### Q: 忘记激活虚拟环境会怎样？

**A:** 如果忘记激活虚拟环境，`pip install` 会安装到系统 Python 环境，可能引起依赖冲突。建议：

1. 确认命令行前缀有 `(venv)`
2. 如果没有，运行 `source venv/bin/activate` （macOS/Linux）或 `venv\Scripts\activate` （Windows）

### Q: 爬虫采用什么技术？

**A:** 本项目使用 **HTML API 爬取模式**，直接访问 vivo 开发者网站的 HTML 页面：

```
https://developers-watch.vivo.com.cn{path}?hastopwindow=1
```

**工作原理：**
1. 从 3 个导航页面（API、Reference、Component）提取侧边栏链接
2. 自动发现所有 161 个文档页面
3. 使用 `?hastopwindow=1` 参数获取完整 HTML 内容
4. 提取 `.html-content` 区域的文档内容

**相比浏览器自动化的优势：**
- ⚡ 速度更快（无需加载浏览器）
- 🎯 数据更准确（直接获取 HTML 内容）
- 💪 稳定性更高（不受页面渲染影响）
- 📦 依赖更少（无需 Playwright）

### Q: 爬取速度太慢怎么办？

**A:** 可以调整以下配置：

1. **缩短延迟**：修改 `config.json` 中的 `delay_range`
   ```json
   "delay_range": [0.5, 1]  // 从 [1, 3] 改为 [0.5, 1]
   ```

2. **减少重试**：降低 `retry_times`（不推荐）

⚠️ **注意**：延迟过短可能触发反爬虫机制，建议保持至少 0.5 秒延迟。

### Q: 爬取失败怎么办？

**A:** 按以下步骤排查：

1. **查看日志**：`crawler.log` 包含详细错误信息
2. **检查网络**：确认可以访问 `developers-watch.vivo.com.cn`
3. **断点续爬**：程序自动记录已爬取页面，直接重新运行即可
4. **手动测试**：
   ```bash
   curl "https://developers-watch.vivo.com.cn/page-data/product/blueos/doc/common/js/system/app/page-data.json"
   ```

### Q: 如何只爬取特定分类？

**A:** 修改 `config.json` 的 `entry_urls`：

```json
// 只爬取 JavaScript API
"entry_urls": [
  "https://developers.vivo.com/product/blueos/doc/common/js/system/app"
]

// 只爬取教程
"entry_urls": [
  "https://developers.vivo.com/product/blueos/doc/common/reference/quickstart/introduction"
]
```

### Q: 如何更新文档？

**A:** 两种方式：

**方式 1：增量更新**（推荐）
```bash
./run.sh  # 自动跳过已爬取页面
```

**方式 2：完全重新爬取**
```bash
rm -rf data/raw/  # 删除原始数据
rm -rf output/    # 删除输出文件
./run.sh          # 重新爬取
```

### Q: 爬取到的数据存储在哪里？

**A:** 
- **原始数据**：`data/raw/*.jsonl`（JSON Lines 格式，每行一个文档）
- **Markdown**：`output/markdown/`（按分类组织的目录结构）
- **LLM 文档**：`output/llm-ready/`（合并的大文档和问答对）

### Q: JSONL 格式如何使用？

**A:** JSONL 是 JSON Lines 格式，每行一个独立的 JSON 对象：

```python
import json

# 读取 JSONL 文件
with open('data/raw/js-api.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        doc = json.loads(line)
        print(doc['title'], doc['url'])
```

### Q: 如何验证爬取结果？

**A:** 检查统计信息：

```bash
cat data/metadata/statistics.json
```

输出示例：
```json
{
  "generated_at": "2025-11-24T01:38:13",
  "total_urls": 150,
  "success_count": 148,
  "failed_count": 2,
  "skipped_count": 0
}
```

## 技术实现细节

### 爬虫架构

```
┌─────────────────┐
│  Entry URLs    │  入口页面配置
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  API Crawler   │  调用 Gatsby page-data API
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Extractors    │  提取标题、正文、代码
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Storage       │  保存 JSONL 格式数据
└─────────────────┘
```

### 核心模块

| 模块 | 文件 | 功能 |
|------|------|------|
| **爬虫调度** | `scheduler_api.py` | 控制爬取流程，管理进度 |
| **API 爬虫** | `api_crawler.py` | 调用 Gatsby API 获取数据 |
| **内容提取** | `extractors.py` | 解析 HTML，提取结构化内容 |
| **数据存储** | `storage.py` | 保存 JSONL 和统计信息 |
| **Markdown 转换** | `markdown_converter.py` | HTML 转 Markdown |
| **LLM 生成器** | `llm_generator.py` | 合并文档、生成问答对 |
| **索引构建** | `index_builder.py` | 构建多维度索引 |

### 数据流程

```
API 爬取 → JSONL 存储 → Markdown 转换 → LLM 优化 → 索引构建
   ↓            ↓              ↓              ↓           ↓
 page-data   raw/*.jsonl   markdown/   llm-ready/   index/
```

## 下一步：扩展应用

基于本项目生成的数据，可以构建：

### 1. MCP 服务器

使用 Model Context Protocol 为 AI 工具提供文档查询：

```python
from mcp import Server
import json

server = Server("vivo-blueos-docs")

@server.tool()
def search_api(name: str):
    with open('output/index/api-index.json') as f:
        index = json.load(f)
    # 搜索逻辑...
```

### 2. RAG 系统

构建检索增强生成系统：

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# 加载文档
docs = load_markdown_docs('output/llm-ready/combined/')

# 构建向量数据库
vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())

# 检索相关文档
results = vectorstore.similarity_search("如何使用 app API？")
```

### 3. VS Code 插件

开发代码补全插件，提供实时文档提示。

### 4. 文档网站

基于 Markdown 文件构建静态文档站点（如 VuePress、Docusaurus）。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

**改进方向：**
- 支持更多文档类型
- 优化内容提取算法
- 增加增量更新机制
- 支持多语言文档

## 许可证

MIT License - 详见 LICENSE 文件
