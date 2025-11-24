#!/bin/bash

# vivo 手表文档爬虫运行脚本

set -e

echo "=================================="
echo "vivo 手表文档爬虫与生成系统"
echo "=================================="

# 检查是否在项目根目录
if [ ! -f "config.json" ]; then
    echo "错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 检查 Python 版本
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python 版本: $python_version"

# 检查依赖是否安装
if ! python3 -c "import requests" 2>/dev/null; then
    echo ""
    echo "正在安装依赖..."
    pip install -r requirements.txt
fi

echo ""
echo "步骤 1/3: 运行vivo手表文档爬虫"
echo "----------------------------------"
python3 -m src.crawler.main

echo ""
echo "步骤 2/3: 运行BlueOS Studio文档爬虫"
echo "----------------------------------"
python3 -m src.crawler.blueos_main

echo ""
echo "步骤 3/3: 转换和生成文档"
echo "----------------------------------"
python3 -m src.converter.main

echo ""
echo "=================================="
echo "所有任务完成!"
echo "=================================="
echo ""
echo "输出文件:"
echo "  - 原始数据: data/raw/"
echo "  - Markdown: output/markdown/"
echo "  - LLM 文档: output/llm-ready/"
echo "  - 索引: output/index/"
echo ""