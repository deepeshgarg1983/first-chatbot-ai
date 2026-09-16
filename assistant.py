from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to Ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("*" * 14)
print("Deepesh CHAT")
print("*" * 14)
print("Type 'exit' to stop.")

while True:

    question = input("\nEnter your question: ")

    # Exit condition
    if question.lower() == "exit":
        print("\n" + "*" * 14)
        print("Goodbye!")
        print("*" * 14)
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\n" + "*" * 14)
    print("OLLAMA RESPONSE")
    print("*" * 14)

    print(response.choices[0].message.content)

    print("*" * 14)