#uv add langgraph-cli[inmem],用LangGraph命令行在本地部署，所以要先安装LangGraph的依赖。
from dotenv import load_dotenv
import os
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage
load_dotenv()
API_KEY =os.getenv("gpt_api_key")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("OPENAI_MODEL")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
web_search = TavilySearch(
    max_results=5,
    topic="general",
)

LLM = ChatOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    model = MODEL_NAME,
)

system_prompt = """
你是一名私人厨师。收到用户提供的食材照片或清单后，请按以下流程操作：
1.识别和评估食材：若用户提供照片，首先辨识所有可见食材。基于食材的外观状态，评估其新鲜度与可用量，整理出一份“当前可用食材清单”。
2.智能食谱检索：优先调用 web_search 工具，以“可用食材清单”为核心关键词，查找可行菜谱。
3.多维度评估与排序：从营养价值和制作难度两个维度对检索到的候选食谱进行量化打分，并根据得分排序，制作简单且营养丰富的排名靠前。
4.结构化方案输出：把排序后的食谱整理为一份结构清晰的建议报告，要包含食谱信息、得分、推荐理由、食谱的参考图片，帮助用户快速做出决策。

请严格按照流程，优先调用 web_search 工具搜索食谱，搜索不到的情况下才能自己发挥。
"""

agent = create_agent(
    model=LLM,
    tools=[web_search],
    system_prompt=system_prompt,
)
# 准备多模态消息，图片是网络上的冰箱食物图片
multimodal_message = HumanMessage(
    content=[
        {"type": "image",
         "url": "https://img.freepik.com/free-photo/arrangement-different-foods-organized-fridge_23-2149099882.jpg"},
        {"type": "text", "text": "帮我看看这些食材能做些什么？"}
    ])

config = {"configurable": {"thread_id": "6"}}

response = agent.invoke({"messages": [multimodal_message]}, config)
# 友好打印
for message in response['messages']:
    message.pretty_print()

response = agent.invoke(
        {"messages": [HumanMessage(content="我喜欢第1道菜，可以说的更详细点吗？")]},
        config
    )

# 友好打印
response['messages'][-1].pretty_print()