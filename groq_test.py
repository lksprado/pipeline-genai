from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def minha_pergunta_pro_groq(pergunta:str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pergunta,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

