import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
    model=os.getenv("MODEL_NAME"),
)

def basic_call(prompt: str) -> str:
    messages = [
        SystemMessage(content="You are a helpful LinkedIn content writer."),
        HumanMessage(content=prompt)
    ]
    response = llm.invoke(messages)
    return response.content.strip()

if __name__ == "__main__":
    result = basic_call("Write one sentence about AI in Healthcare for LinkedIn.")
    print("Basic Agent Output:")
    print(result)