import requests
import config 

API_URL = "https://api.openai.com/v1/chat/completions"

def chat_with_ai(user_message):
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Greeting message
print("Hi there! I am Markhor, the AI chatbot powered by ChatGPT-4, represented by Coding Moves.")
print("How can I assist you today?\n")

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Markhor AI: Goodbye! Have a great day.")
        break
    bot_response = chat_with_ai(user_input)
    print("Markhor AI:", bot_response)
