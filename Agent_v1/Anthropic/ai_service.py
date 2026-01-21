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

class CustomerServiceBot:
    "AI助手"

    def __init__(self):
        self.model = model

        self.system_prompt = SystemMessage(content="你是一個樂於助人的聊天機器人。你使用繁體中文與用戶對話。 職責:熱情歡迎用戶、記住用戶訊息(姓名、問題等)、提供準確的幫助、結束時禮貌道別。 風格:語氣友好、簡潔明瞭、使用表情符號增加親和力。")

        self.history = [self.system_prompt]

    def chat(self, user_input: str) -> str:
        # 添加用戶訊息
        self.history.append(HumanMessage(content=user_input))
        # 調用模型
        response = self.model.invoke(self.history)
        # 添加AI回覆到歷史  
        self.history.append(AIMessage(content=response.content))
        return response.content
    
    def get_history_length(self) -> int:
        # 獲得對話長度
        return len(self.history)
    
    def clear_history(self):
        # 清空歷史
        self.history = [self.system_prompt]

bot = CustomerServiceBot()

while True:
    user_input = input("User: ")
    result = bot.chat(user_input)
    print(f"AI: {result}\n")

