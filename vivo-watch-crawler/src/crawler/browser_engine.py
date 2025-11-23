"""
HTTP 请求引擎模块

负责发送 HTTP 请求并获取页面内容
"""

import logging
import time
import random
from typing import Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


class HTTPEngine:
    """HTTP 请求引擎"""
    
    def __init__(self, user_agent: Optional[str] = None, timeout: int = 30):
        """
        初始化 HTTP 引擎
        
        Args:
            user_agent: 自定义 User-Agent
            timeout: 请求超时时间（秒）
        """
        self.timeout = timeout
        self.session = requests.Session()
        
        # 配置重试策略
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # 设置默认请求头
        default_ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.session.headers.update({
            'User-Agent': user_agent or default_ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
    def get_page(self, url: str) -> Optional[str]:
        """
        获取页面内容
        
        Args:
            url: 目标 URL
            
        Returns:
            页面 HTML 内容，失败返回 None
        """
        try:
            logger.info(f"请求页面: {url}")
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # 检查内容类型
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type:
                logger.warning(f"非 HTML 内容: {content_type}")
                return None
            
            # 确保使用正确的编码
            response.encoding = response.apparent_encoding
            
            logger.info(f"成功获取页面: {url} (长度: {len(response.text)})")
            return response.text
            
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP 错误: {url}, 状态码: {e.response.status_code}")
            return None
        except requests.exceptions.Timeout:
            logger.error(f"请求超时: {url}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"请求失败: {url}, 错误: {str(e)}")
            return None
    
    def close(self):
        """关闭 session"""
        self.session.close()
        logger.info("HTTP 引擎已关闭")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    engine = HTTPEngine()
    html = engine.get_page(
        "https://developers.vivo.com/product/blueos/doc/common/reference/quickstart/introduction"
    )
    if html:
        print(f"HTML 长度: {len(html)}")
        print(f"前 200 字符: {html[:200]}")
    engine.close()
