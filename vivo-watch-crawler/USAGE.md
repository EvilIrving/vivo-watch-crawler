# vivo 手表文档爬虫使用指南

## 项目概述

本项目用于自动爬取 vivo BlueOS 手表开发文档，并转换为适合大语言模型（LLM）使用的 Markdown 格式文档。采用高效的 API 爬取策略，直接从 Gatsby 页面数据接口获取内容，无需浏览器自动化工具。

### 核心功能

- 🚀 **API 爬取模式**：直接调用 Gatsby page-data API，速度快、稳定性高
- 📑 **智能分类**：自动识别教程(tutorial)、JS API、UI 组件三大类别
- 🔍 **内容提取**：精准提取标题、正文、代码示例及元数据
- 📝 **格式转换**：HTML 转 Markdown，保持代码示例格式
- 🤖 **LLM 优化**：生成合并文档和问答对数据集
- 📊 **索引构建**：为文档搜索和 MCP 服务提供索引支持

## 快速开始

### 1. 安装依赖

```bash
cd vivo-watch-crawler
pip install -r requirements.txt
```

> **注意**：本项目使用 API 爬取模式，不需要安装 Playwright 或浏览器驱动。

### 2. 一键运行（推荐）

```bash
chmod +x run.sh
./run.sh
```

**执行流程：**
1. 自动检查 Python 环境和依赖
2. 从 sitemap 发现所有页面
3. 通过 API 批量爬取页面数据
4. 转换 HTML 为 Markdown 格式
5. 生成 LLM 就绪的合并文档
6. 构建多维度索引文件

**预计用时：** 约 2-5 分钟（取决于网络速度和页面数量）

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

### Q: 爬虫采用什么技术？

**A:** 本项目使用 **API 爬取模式**，直接调用 vivo 开发者网站的 Gatsby page-data API：

```
https://developers-watch.vivo.com.cn/page-data{path}/page-data.json
```

这种方式相比浏览器自动化具有以下优势：
- ⚡ 速度更快（无需加载浏览器）
- 🎯 数据更准确（直接获取结构化数据）
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
