from typing import Literal

from tavily import TavilyClient

from config import TOML_CONFIG

tavily_client = TavilyClient(api_key=TOML_CONFIG.search_config.api_key)


def internet_search(
        query: str,
        max_results: int = 5,
        topic: Literal["general", "news", "finance"] = "general",
        include_raw_content: bool = False,
):
    """
    执行互联网查询

    Args:
        query: 查询语句
        max_results: 最大返回数量
        topic: 主题
        include_raw_content: 是否包含原始内容
    """

    return tavily_client.search(
        query,
        max_results=max_results,
        topic=topic,
        include_raw_content=include_raw_content
    )
