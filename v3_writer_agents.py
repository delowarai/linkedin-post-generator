import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
    model=os.getenv("MODEL_NAME"),
    temperature=0.7,
)

tech_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert Tech Writer for LinkedIn.
Rules:
- Write in {language}
- 2 to 4 short paragraphs
- Professional and insightful tone
- End with a question or call-to-action
- Use 1 to 3 emojis tastefully
- Write the post directly, no preamble"""),
    ("human", "Write a LinkedIn post about: {topic}")
])

general_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert General Content Writer for LinkedIn.
Rules:
- Write in {language}
- 2 to 4 short paragraphs
- Warm, mentor-like professional tone
- End with a question or call-to-action
- Use 1 to 3 emojis tastefully
- Write the post directly, no preamble"""),
    ("human", "Write a LinkedIn post about: {topic}")
])

def tech_writer_agent(topic: str, language: str) -> str:
    print(f"\n[Tech Writer Agent] Writing about '{topic}' in {language}...")
    chain = tech_prompt | llm
    response = chain.invoke({"topic": topic, "language": language})
    post = response.content.strip()
    print(f"   Tech post ready! ({len(post)} chars)")
    return post

def general_writer_agent(topic: str, language: str) -> str:
    print(f"\n[General Writer Agent] Writing about '{topic}' in {language}...")
    chain = general_prompt | llm
    response = chain.invoke({"topic": topic, "language": language})
    post = response.content.strip()
    print(f"   General post ready! ({len(post)} chars)")
    return post

if __name__ == "__main__":
    tech_post = tech_writer_agent("AI in Healthcare", "English")
    print(f"\n--- TECH POST ---\n{tech_post}\n")
    general_post = general_writer_agent("Remote Work Productivity", "Bangla")
    print(f"\n--- GENERAL POST ---\n{general_post}\n")