from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from dotenv import load_dotenv
import os

load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

model = ChatAnthropic(
    model_name="claude-haiku-4-5-20251001",
    temperature=0,
    api_key=anthropic_api_key
)

conversation_histroy = []

def chat(user_input):
    # 增加用戶訊息
    conversation_histroy.append(HumanMessage(content=user_input))
    # 調用模型
    response = model.invoke(conversation_histroy)
    # 增加AI回復到歷史
    conversation_histroy.append(AIMessage(content=response.content))
    return response.content

while True:
    user_input = input("User: ")
    result = chat(user_input)
    print(f"AI: {result}\n")