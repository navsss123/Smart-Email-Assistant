import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create OpenAI client using the new SDK format
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(text):
    prompt = (
        "Based on this email, write a polite and relevant reply:\n\n" + text
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error: {e}"
