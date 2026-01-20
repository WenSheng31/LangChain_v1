from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain_core.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

@tool
def get_weather(loacl: str) -> str:
    "查詢指定城市的天氣情況"
    return f"{loacl}的天氣是晴天，氣溫25度。"

model = ChatAnthropic(
    model_name = "claude-haiku-4-5-20251001",
    temperature=0,
    api_key=anthropic_api_key
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一個樂於助人的聊天機器人。你使用繁體中文與用戶對話。"
)