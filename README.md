# vivo 手表文档爬虫与 LLM 文档生成系统

⚠️ **重要说明**

本项目已归档。**vivo 不支持个人开发者发布应用**。本项目仅供学习参考，不可用于商业用途。

---

## 项目简介

本项目用于爬取 vivo BlueOS 手表开发文档，并转换为适合大模型（LLM）训练和使用的 Markdown 格式文档。

## MCP 服务

本项目包含 MCP（Model Context Protocol）服务器实现，用于为 LLM 提供文档检索和索引功能。

详见：[mcp-server/README.md](mcp-server/README.md)

## 功能特性
ß
- ✅ 支持 JavaScript 动态渲染页面的爬取
- ✅ 自动提取侧边栏导航结构
- ✅ 智能提取页面内容和代码示例
- ✅ 生成 LLM 友好的 Markdown 文档
- ✅ 构建文档索引（为 MCP 服务准备）

## 目录结构

```
vivo-watch-crawler/
├── data/                    # 爬取的原始数据
│   ├── raw/                # JSON Lines 格式的原始数据
│   ├── navigation/         # 站点导航结构
│   └── metadata/           # 爬取日志和统计信息
├── output/                  # 输出文档
│   ├── markdown/           # 分类的 Markdown 文档
│   ├── llm-ready/          # LLM 就绪的合并文档
│   └── index/              # 索引文件
├── src/                     # 源代码
│   ├── crawler/            # 爬虫模块
│   ├── converter/          # 转换器模块
│   └── generator/          # 生成器模块
└── requirements.txt         # Python 依赖
```

## 快速开始

### 0. 环境要求

- Python 3.8+
- pip
- 网络连接（需访问 developers-watch.vivo.com.cn 和 studio.blueos.com.cn）

### 1. 创建虚拟环境（推荐）

**macOS/Linux:**
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate
```

**Windows:**
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

> **注意**：本项目使用 HTML API 爬取模式，**无需安装** Playwright 或浏览器驱动。

### 3. 运行爬虫

**一键运行（推荐）:**
```bash
chmod +x run.sh
./run.sh
```

**或分步运行:**
```bash
# 爬取vivo手表文档
python -m src.crawler.main

# 爬取BlueOS Studio文档
python -m src.crawler.blueos_main

# 转换为 Markdown
python -m src.converter.main
```

### 4. 生成 LLM 文档

运行 `./run.sh` 会自动完成以下步骤：
1. 爬取所有文档（包括vivo手表文档和BlueOS Studio文档）
2. 转换为 Markdown 格式
3. 生成 LLM 就绪文档
4. 构建文档索引

### 5. 清理环境

**退出虚拟环境:**
```bash
deactivate
```

**删除虚拟环境:**
```bash
rm -rf venv/
```

**清理数据（重新爬取）:**
```bash
rm -rf data/ output/
```

## 配置说明

配置文件：`config.json`

- `entry_urls`: 入口 URL 列表
- `max_workers`: 最大并发数
- `retry_times`: 失败重试次数
- `delay_range`: 请求延迟范围（秒）

## 输出说明

- `data/raw/*.jsonl`: 原始爬取数据
- `output/markdown/`: 分类的 Markdown 文档
- `output/llm-ready/combined/`: 合并的大文档
- `output/llm-ready/qa-pairs/`: 问答对数据集
- `output/index/`: 索引文件（为 MCP 准备）

## 许可证

MIT