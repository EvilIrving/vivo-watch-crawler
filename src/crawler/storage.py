"""
数据存储模块

负责将爬取的数据保存为 JSON Lines 格式
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Any, Optional

logger = logging.getLogger(__name__)


class DataStorage:
    """数据存储层"""
    
    def __init__(self, data_dir: str = "data"):
        """
        初始化数据存储
        
        Args:
            data_dir: 数据目录
        """
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.navigation_dir = self.data_dir / "navigation"
        self.metadata_dir = self.data_dir / "metadata"
        
        # 确保目录存在
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.navigation_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
        
        # 爬取日志文件
        self.crawl_log_file = self.metadata_dir / "crawl-log.jsonl"
        
    def save_page_data(self, url: str, category: str, content: dict, status: str = "success"):
        """
        保存页面数据到 JSON Lines 文件
        
        Args:
            url: 页面 URL
            category: 分类（tutorial/js-api/ui-component）
            content: 提取的内容
            status: 爬取状态
        """
        # 根据分类确定文件名
        category_files = {
            'tutorial': 'tutorial.jsonl',
            'js-api': 'js-api.jsonl',
            'ui-component': 'ui-component.jsonl'
        }
        
        filename = category_files.get(category, 'other.jsonl')
        filepath = self.raw_dir / filename
        
        # 构建数据记录
        record = {
            'url': url,
            'category': category,
            'crawl_time': datetime.now().isoformat(),
            'status': status,
            **content
        }
        
        # 追加写入 JSON Lines 文件
        try:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
            logger.info(f"保存页面数据: {url} -> {filename}")
        except Exception as e:
            logger.error(f"保存页面数据失败: {url}, 错误: {str(e)}")
            
    def save_navigation_structure(self, structure: dict, filename: str = "site-structure.json"):
        """
        保存站点导航结构
        
        Args:
            structure: 导航结构
            filename: 文件名
        """
        filepath = self.navigation_dir / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(structure, f, ensure_ascii=False, indent=2)
            logger.info(f"保存导航结构: {filename}")
        except Exception as e:
            logger.error(f"保存导航结构失败: {str(e)}")
            
    def log_crawl_event(self, event_type: str, url: str, details: Optional[dict] = None):
        """
        记录爬取事件
        
        Args:
            event_type: 事件类型（start/success/error/skip）
            url: URL
            details: 详细信息
        """
        event = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'url': url,
            'details': details or {}
        }
        
        try:
            with open(self.crawl_log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(event, ensure_ascii=False) + '\n')
        except Exception as e:
            logger.error(f"记录爬取事件失败: {str(e)}")
            
    def save_statistics(self, stats: dict):
        """
        保存爬取统计信息
        
        Args:
            stats: 统计信息
        """
        filepath = self.metadata_dir / "statistics.json"
        
        stats_with_time = {
            'generated_at': datetime.now().isoformat(),
            **stats
        }
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(stats_with_time, f, ensure_ascii=False, indent=2)
            logger.info("保存统计信息")
        except Exception as e:
            logger.error(f"保存统计信息失败: {str(e)}")
            
    def load_crawled_urls(self) -> set:
        """
        加载已爬取的 URL 列表（用于断点续爬）
        
        Returns:
            已爬取的 URL 集合
        """
        crawled_urls = set()
        
        # 从所有 jsonl 文件中读取已爬取的 URL
        for jsonl_file in self.raw_dir.glob("*.jsonl"):
            try:
                with open(jsonl_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            record = json.loads(line)
                            if record.get('status') == 'success':
                                crawled_urls.add(record.get('url'))
            except Exception as e:
                logger.warning(f"读取已爬取 URL 失败: {jsonl_file}, 错误: {str(e)}")
                
        logger.info(f"加载已爬取 URL: {len(crawled_urls)} 个")
        return crawled_urls
        
    def read_jsonl(self, filename: str) -> list:
        """
        读取 JSON Lines 文件
        
        Args:
            filename: 文件名
            
        Returns:
            记录列表
        """
        filepath = self.raw_dir / filename
        records = []
        
        if not filepath.exists():
            return records
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        records.append(json.loads(line))
        except Exception as e:
            logger.error(f"读取 JSON Lines 文件失败: {filename}, 错误: {str(e)}")
            
        return records
