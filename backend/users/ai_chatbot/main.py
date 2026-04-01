from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# 🔹 LLM setup
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


# 🔹 MAIN FUNCTION
def get_ai_response(user_query):
    try:
        prompt = f"""
You are Senpai, an expert in anime, manga, and manhwa.

PERSONALITY:
- Friendly, confident, slightly cool 
- Talk like an anime senpai (natural, not cringe)

BEHAVIOR RULES:

1. If user says greeting (hi, hello, hey):
   → Reply casually in 1–2 lines only

2. If user asks anime/manga/manhwa related question:
   → Give structured recommendations

FORMAT for recommendations:

🎌 Top Picks

1. <Name> - <short description>
2. <Name> - <short description>
3. <Name> - <short description>

 Recommendation: <one line suggestion>

3. Keep responses SHORT
4. NO long paragraphs
5. NO unnecessary explanation

User:
{user_query}
"""

        # 🔹 Call LLM
        response = llm.invoke(prompt)
        text = response.content.strip()

        #  OPTIONAL SAFETY (limit very long responses)
        if len(text) > 800:
            text = text[:800] + "..."

        return {
            "topic": user_query,
            "summary": text,
            "sources": [],
            "tools_used": ["senpai_smart_v2"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }