import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
    model=os.getenv("MODEL_NAME"),
    temperature=0.1,
)

router_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a topic classification agent.
Classify the topic as 'tech' or 'general'.

Tech: AI, ML, Software, Cloud, Blockchain, Cybersecurity, IoT, DevOps, FinTech, Data Science.
General: Leadership, Remote Work, Career, Marketing, HR, Productivity, Mental Health, Education.

Respond ONLY with valid JSON:
{{"category": "tech", "reason": "brief reason"}}"""),
    ("human", "Classify this topic: {topic}")
])

def router_agent(topic: str) -> dict:
    print(f"\n[Router Agent] Analyzing: '{topic}'")
    chain = router_prompt | llm
    response = chain.invoke({"topic": topic})
    raw = response.content.strip().replace("```json", "").replace("```", "").strip()
    result = json.loads(raw)
    print(f"   Result: {result['category'].upper()} - {result['reason']}")
    return result

if __name__ == "__main__":
    topics = ["AI in Healthcare", "Remote Work Productivity", "Blockchain in Finance", "Leadership Skills"]
    for topic in topics:
        result = router_agent(topic)
        print(f"   -> {topic}: {result['category'].upper()}\n")