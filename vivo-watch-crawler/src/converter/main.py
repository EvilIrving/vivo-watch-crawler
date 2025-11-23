"""
转换器和生成器主程序

用法:
    python -m src.converter.main
"""

import json
import logging
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.converter.markdown_converter import MarkdownConverter
from src.generator.llm_generator import LLMDocGenerator
from src.generator.index_builder import IndexBuilder


def setup_logging():
    """配置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('converter.log', encoding='utf-8')
        ]
    )


def load_config(config_path: str = 'config.json') -> dict:
    """加载配置文件"""
    config_file = project_root / config_path
    
    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_file}")
        
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
        
    return config


def main():
    """主函数"""
    # 配置日志
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("=" * 60)
        logger.info("开始文档转换和生成")
        logger.info("=" * 60)
        
        # 加载配置
        config = load_config()
        
        data_dir = Path(config.get('data_dir', 'data'))
        output_dir = Path(config.get('output_dir', 'output'))
        
        # 阶段 1: 转换为 Markdown
        logger.info("\n阶段 1: HTML 转 Markdown")
        logger.info("-" * 60)
        
        markdown_converter = MarkdownConverter(str(output_dir / 'markdown'))
        
        # 读取所有原始数据并转换
        raw_dir = data_dir / 'raw'
        total_converted = 0
        
        for jsonl_file in raw_dir.glob("*.jsonl"):
            logger.info(f"\n处理文件: {jsonl_file.name}")
            
            with open(jsonl_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        record = json.loads(line)
                        if record.get('status') == 'success':
                            category = record.get('category', 'other')
                            result = markdown_converter.convert_page(record, category)
                            
                            if result:
                                markdown_converter.save_markdown(
                                    result['filepath'],
                                    result['markdown']
                                )
                                total_converted += 1
                                
        logger.info(f"\n转换完成: {total_converted} 个文档")
        
        # 阶段 2: 生成 LLM 文档
        logger.info("\n阶段 2: 生成 LLM 就绪文档")
        logger.info("-" * 60)
        
        llm_generator = LLMDocGenerator(str(output_dir / 'llm-ready'))
        
        # 合并文档
        markdown_dir = output_dir / 'markdown'
        llm_generator.process_markdown_files(markdown_dir)
        
        # 生成问答对
        llm_generator.generate_qa_pairs(data_dir)
        
        # 阶段 3: 构建索引
        logger.info("\n阶段 3: 构建索引")
        logger.info("-" * 60)
        
        index_builder = IndexBuilder(str(output_dir / 'index'))
        index_builder.build_all_indexes(data_dir, markdown_dir)
        
        # 完成
        logger.info("\n" + "=" * 60)
        logger.info("所有任务完成!")
        logger.info("=" * 60)
        logger.info(f"\n输出目录:")
        logger.info(f"  - Markdown 文档: {markdown_dir}")
        logger.info(f"  - LLM 文档: {output_dir / 'llm-ready'}")
        logger.info(f"  - 索引文件: {output_dir / 'index'}")
        
    except Exception as e:
        logger.error(f"\n转换过程中发生错误: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    # 切换到项目根目录
    import os
    os.chdir(project_root)
    
    # 运行主程序
    main()
