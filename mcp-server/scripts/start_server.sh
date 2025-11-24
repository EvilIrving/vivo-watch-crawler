#!/bin/bash
# BlueOS MCP 服务器启动脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "========================================="
echo "BlueOS 文档 MCP 服务器启动工具"
echo "========================================="
echo ""

# 检查虚拟环境
if [ ! -d "$PROJECT_ROOT/venv" ]; then
    echo "虚拟环境不存在，正在创建..."
    python3 -m venv "$PROJECT_ROOT/venv"
    echo "✓ 虚拟环境已创建"
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source "$PROJECT_ROOT/venv/bin/activate"

# 检查依赖
if ! python -c "import mcp" 2>/dev/null; then
    echo "依赖未安装，正在安装..."
    pip install -q -r "$PROJECT_ROOT/requirements.txt"
    echo "✓ 依赖已安装"
fi

# 检查数据文件
if [ ! -f "$PROJECT_ROOT/data/resource-refs.json" ]; then
    echo ""
    echo "资源引用映射表不存在，正在构建..."
    python "$PROJECT_ROOT/scripts/build_refs.py"
    echo ""
fi

if [ ! -f "$PROJECT_ROOT/data/rules-knowledge-base.json" ]; then
    echo ""
    echo "规则知识库不存在，正在提取..."
    python "$PROJECT_ROOT/scripts/extract_rules.py"
    echo ""
fi

# 启动服务器
echo ""
echo "========================================="
echo "启动 MCP 服务器 (STDIO 模式)"
echo "========================================="
echo ""

cd "$PROJECT_ROOT"
python -m src.server --transport stdio
