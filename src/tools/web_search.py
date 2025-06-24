from langchain_tavily import TavilySearch
from langchain.tools import tool

# 创建 TavilySearch 实例
_tavily_search = TavilySearch(
    name="web_search",
    max_results=5,
)

@tool
def web_search(query: str) -> str:
    """
    Search the web for information about a given query.
    
    Args:
        query: The search query string.
        
    Returns:
        Search results as a string.
    """
    try:
        results = _tavily_search.invoke(query)
        return str(results)
    except Exception as e:
        return f"搜索失败: {e}"