"""
BlueOS Studio 爬虫主程序入口

用法:
    python -m src.crawler.blueos_main
"""

import json
import logging
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.crawler.blueos_scheduler import BlueOSScheduler


def setup_logging():
    """配置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('blueos_crawler.log', encoding='utf-8')
        ]
    )


def load_config(config_path: str = 'config.json') -> dict:
    """
    加载配置文件
    
    Args:
        config_path: 配置文件路径
        
    Returns:
        配置字典
    """
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
        # 加载配置
        logger.info("加载配置文件...")
        config = load_config()
        
        # 创建并启动调度器
        scheduler = BlueOSScheduler(config)
        scheduler.start()
        
        logger.info("\n所有任务完成!")
        
    except KeyboardInterrupt:
        logger.info("\n用户中断爬取")
    except Exception as e:
        logger.error(f"\n爬取过程中发生错误: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    # 切换到项目根目录
    import os
    os.chdir(project_root)
    
    # 运行主程序
    main()