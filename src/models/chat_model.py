import os

from langchain_openai import ChatOpenAI

# 豆包模型配置
chat_model_doubao = ChatOpenAI(
    model="doubao-1-5-pro-32k-250115",
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.getenv("DOUBAO_API_KEY"),
    temperature=0,
)

# OpenAI模型配置（备用）
chat_model = ChatOpenAI(
    model="gpt-4o",
    base_url="https://api.openai.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0,
)
