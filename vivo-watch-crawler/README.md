# vivo 手表文档爬虫与 LLM 文档生成系统

## 项目简介

本项目用于爬取 vivo BlueOS 手表开发文档，并转换为适合大模型（LLM）训练和使用的 Markdown 格式文档。

## 功能特性

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

### 1. 安装依赖

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 运行爬虫

```bash
python src/crawler/main.py
```

### 3. 生成 LLM 文档

```bash
python src/converter/main.py
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
