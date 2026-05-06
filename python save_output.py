"""
save_output.py
===============
Run this after v4_linkedin_generator.py
Saves Bangla post correctly to a text file
"""

import sys
import io
import os
from dotenv import load_dotenv
from v2_router_agent import router_agent
from v3_writer_agents import tech_writer_agent, general_writer_agent

load_dotenv()

def linkedin_post_generator(topic: str, language: str) -> dict:
    classification = router_agent(topic)
    category = classification["category"]
    reason = classification["reason"]

    if category == "tech":
        writer_used = "Tech Writer Agent"
        post = tech_writer_agent(topic, language)
    else:
        writer_used = "General Writer Agent"
        post = general_writer_agent(topic, language)

    return {
        "topic": topic,
        "language": language,
        "category": category,
        "classification_reason": reason,
        "writer_agent": writer_used,
        "linkedin_post": post
    }

if __name__ == "__main__":

    print("Generating posts...")

    result1 = linkedin_post_generator("AI in Healthcare", "English")
    result2 = linkedin_post_generator("Remote Work Productivity", "Bangla")

    # Save with UTF-8 BOM encoding — works perfectly in VS Code and Notepad
    with open("linkedin_output.txt", "w", encoding="utf-8-sig") as f:
        f.write("=" * 55 + "\n")
        f.write("EXAMPLE 1: Tech Topic - English\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"Topic  : {result1['topic']}\n")
        f.write(f"Lang   : {result1['language']}\n")
        f.write(f"Type   : {result1['category'].upper()}\n")
        f.write(f"Writer : {result1['writer_agent']}\n")
        f.write("-" * 55 + "\n\n")
        f.write(result1['linkedin_post'])
        f.write("\n\n\n")

        f.write("=" * 55 + "\n")
        f.write("EXAMPLE 2: General Topic - Bangla\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"Topic  : {result2['topic']}\n")
        f.write(f"Lang   : {result2['language']}\n")
        f.write(f"Type   : {result2['category'].upper()}\n")
        f.write(f"Writer : {result2['writer_agent']}\n")
        f.write("-" * 55 + "\n\n")
        f.write(result2['linkedin_post'])
        f.write("\n")

    print("\nDone! Open linkedin_output.txt in VS Code")