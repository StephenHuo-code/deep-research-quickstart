import os

from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(
    model="doubao-1-5-pro-32k-250115",
    base_url="https://ark-cn-beijing.bytedance.net/api/v3",
    api_key=os.getenv("DOUBAO_API_KEY"), # 你需要自己设置环境变量
    temperature=0,
)