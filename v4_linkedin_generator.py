import os
from dotenv import load_dotenv
from v2_router_agent import router_agent
from v3_writer_agents import tech_writer_agent, general_writer_agent

load_dotenv()

def linkedin_post_generator(topic: str, language: str) -> dict:
    print("\n" + "=" * 55)
    print("  LinkedIn Post Generator — Agent Started")
    print("=" * 55)
    print(f"  Topic    : {topic}")
    print(f"  Language : {language}")
    print("=" * 55)

    classification = router_agent(topic)
    category = classification["category"]
    reason = classification["reason"]

    print(f"\n[Routing] '{category.upper()}' topic detected")
    print(f"   Reason: {reason}")

    if category == "tech":
        print("   -> Sending to Tech Writer Agent...")
        writer_used = "Tech Writer Agent"
        post = tech_writer_agent(topic, language)
    else:
        print("   -> Sending to General Writer Agent...")
        writer_used = "General Writer Agent"
        post = general_writer_agent(topic, language)

    print("\n" + "=" * 55)
    print("  Agent Completed!")
    print("=" * 55)

    return {
        "topic": topic,
        "language": language,
        "category": category,
        "classification_reason": reason,
        "writer_agent": writer_used,
        "linkedin_post": post
    }

def display_result(result: dict):
    print(f"""
FINAL LINKEDIN POST
{"=" * 50}
Topic  : {result['topic']}
Lang   : {result['language']}
Type   : {result['category'].upper()}
Writer : {result['writer_agent']}
{"=" * 50}

{result['linkedin_post']}

{"-" * 50}
""")

def save_output(result1: dict, result2: dict):
    with open("linkedin_output.txt", "w", encoding="utf-8") as f:
        f.write("=" * 55 + "\n")
        f.write("  EXAMPLE 1: Tech Topic - English\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"Topic  : {result1['topic']}\n")
        f.write(f"Lang   : {result1['language']}\n")
        f.write(f"Type   : {result1['category'].upper()}\n")
        f.write(f"Writer : {result1['writer_agent']}\n")
        f.write("-" * 55 + "\n\n")
        f.write(result1['linkedin_post'])
        f.write("\n\n")
        f.write("=" * 55 + "\n")
        f.write("  EXAMPLE 2: General Topic - Bangla\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"Topic  : {result2['topic']}\n")
        f.write(f"Lang   : {result2['language']}\n")
        f.write(f"Type   : {result2['category'].upper()}\n")
        f.write(f"Writer : {result2['writer_agent']}\n")
        f.write("-" * 55 + "\n\n")
        f.write(result2['linkedin_post'])
        f.write("\n")
    print("\nOutput saved to: linkedin_output.txt")
    print("Open it in VS Code to see Bangla text correctly!")

if __name__ == "__main__":
    result1 = linkedin_post_generator("AI in Healthcare", "English")
    display_result(result1)

    result2 = linkedin_post_generator("Remote Work Productivity", "Bangla")
    display_result(result2)

    save_output(result1, result2)