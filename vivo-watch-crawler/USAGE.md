# 使用说明

## 项目概述

本项目包含两个独立的爬虫系统：

1. **vivo手表文档爬虫** - 爬取 https://developers-watch.vivo.com.cn/ 站点
2. **BlueOS Studio爬虫** - 爬取 https://studio.blueos.com.cn/ 站点

## 运行方式

### 一键运行（推荐）

```bash
chmod +x run.sh
./run.sh
```

该脚本会依次运行：
1. vivo手表文档爬虫
2. BlueOS Studio爬虫
3. 文档转换和生成工具

### 单独运行各个组件

#### 1. 运行vivo手表文档爬虫

```bash
python -m src.crawler.main
```

#### 2. 运行BlueOS Studio爬虫

```bash
python -m src.crawler.blueos_main
```

#### 3. 运行文档转换工具

```bash
python -m src.converter.main
```

## 配置文件

主要配置文件为 `config.json`，包含以下关键配置项：

- `timeout`: 请求超时时间（秒）
- `delay_range`: 请求间隔时间范围（秒）
- `user_agent`: HTTP请求使用的User-Agent
- `data_dir`: 数据存储目录
- `output_dir`: 输出目录

## 输出目录结构

```
data/
├── raw/                 # 原始JSON数据
├── navigation/          # 导航结构数据
└── metadata/            # 元数据和统计信息

output/
├── markdown/            # Markdown格式文档
│   ├── js-api/         # JS API文档
│   ├── tutorial/       # 教程文档
│   ├── ui-component/   # UI组件文档
│   └── blueos-explore/ # BlueOS探索文档
│   └── blueos-write/   # BlueOS写作文档
├── llm-ready/           # LLM就绪文档
└── index/               # 索引文件
```

## BlueOS Studio爬虫详细说明

### 支持的页面类型

1. **探索页面** (`/explore/*`) - 介绍性内容和入门指南
2. **写作页面** (`/write/*`) - 开发指导和组件创建指南
3. **部署页面** (`/deploy/*`) - 构建和发布指南

### 爬虫特点

- 自动从侧边栏发现所有文档链接
- 智能识别页面主要内容区域
- 提取代码示例和文档标题
- 支持断点续传（跳过已爬取页面）

### 自定义页面发现

如果自动发现功能无法正确识别所有页面，可以在 [blueos_studio_crawler.py](src/crawler/blueos_studio_crawler.py) 文件中修改 [_get_predefined_paths](file:///Users/actor/Documents/learn%20self/python/vivo-watch-crawler/src/crawler/blueos_studio_crawler.py#L188-L202) 方法来添加预定义的页面路径。