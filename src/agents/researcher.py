from langgraph.prebuilt import create_react_agent

from src.models.chat_model import chat_model
from src.tools.web_crawl import web_crawl
from src.tools.web_search import web_search

researcher = create_react_agent(
    chat_model,
    tools=[web_search, web_crawl],
    name="researcher",
)

import uuid
import os
from typing import Optional
from langgraph.graph.graph import CompiledGraph
from src.agents.researcher import researcher


def run_agent_stream(agent: CompiledGraph, message: str, thread_id: Optional[str] = None) -> None:
    """
    运行 agent 并流式输出结果
    
    Args:
        agent: 编译后的 LangGraph agent
        message: 用户输入的消息
        thread_id: 线程ID，用于会话持续性
    """
    if thread_id is None:
        thread_id = str(uuid.uuid4())
    
    print(f"🤖 正在处理您的问题: {message}")
    print(f"📝 会话ID: {thread_id}")
    print("=" * 50)
    
    try:
        result = agent.stream(
            {"messages": [{"role": "user", "content": message}]},
            stream_mode="values",
            config={"configurable": {"thread_id": thread_id}},
        )
        
        for chunk in result:
            if "messages" in chunk and chunk["messages"]:
                last_message = chunk["messages"][-1]
                last_message.pretty_print()
                print("-" * 30)
                
    except Exception as e:
        print(f"❌ 运行 agent 时出错: {e}")





def main():
    """主函数"""
    run_agent_stream(researcher, "你好，请简单介绍一下自己的能力")

if __name__ == "__main__":
    main()