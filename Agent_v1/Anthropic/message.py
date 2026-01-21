from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from dotenv import load_dotenv
import os

load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

model = ChatAnthropic(
    model_name="claude-haiku-4-5-20251001",
    max_tokens_to_sample=200,
    temperature=0,
    api_key=anthropic_api_key
)


# # 字典格式
# msg_dict = [
#     {"role": "system", "content": "你是一個樂於助人的聊天機器人。你使用繁體中文與用戶對話。"},
#     {"role": "user", "content": "你是誰？"},
#     {"role": "assistant", "content": "我是你媽"},
#     {"role": "user", "content": "你好媽媽"}
# ]

# for msg in msg_dict:
#     print(f"{msg['role']}: {msg['content']}")

# response = model.invoke(msg_dict)
# print(f"AI: {response.content}")


# 消息對象
msg_obj = [
    SystemMessage("你是一個樂於助人的聊天機器人。你使用繁體中文與用戶對話。"),
    HumanMessage("你是誰？"),
    AIMessage("我是你媽"),
    HumanMessage("你好媽媽")
]

for msg in msg_obj:
    print(f"{msg.type}: {msg.content}")

response = model.invoke(msg_obj)
print(f"AI: {response.content}")