from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Lade den API-Key aus der .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Testanfrage an GPT schicken
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Erkläre in einem Satz, was ein Vertrag ist."}
    ]
)

# 3. Antwort ausgeben
print(response.choices[0].message.content)
