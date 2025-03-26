# 🤖 AI Chatbot on Python  

Welcome to **Markhor AI Chatbot**, a Python-based chatbot powered by **ChatGPT-4**! 🚀  
This chatbot is designed to have intelligent conversations using OpenAI's API.

---

## 🌟 Features  

✅ Uses **GPT-4 API** for natural conversations  
✅ Interactive **CLI chat interface**  
✅ Secure API key handling using `.gitignore`  
✅ Simple and **easy-to-use Python script**  
✅ Exit command (`exit`, `quit`, `bye`) to stop the chat  


---

## 🛠️ Installation  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Muawiya-contact/AI-Chatbot-on-Python.git
cd AI-Chatbot-on-Python
```


### **2️⃣ Create a Virtual Environment (Recommended)**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Required Dependencies**  
```sh
pip install -r requirements.txt
```

---

## 🔑 Secure API Key Handling  

**DO NOT** hardcode your API key in the script! Instead, follow these steps:  

1. **Create a `config.py` file** in the project directory:  
   ```python
   API_KEY = "your-secret-api-key"
   ```
2. **Add `config.py` to `.gitignore`** to prevent it from being uploaded:  
   ```
   config.py
   ```
3. **Now, import the key securely in your script:**  
   ```python
   from config import API_KEY
   ```

---

## 🚀 Usage  

1. **Run the chatbot**:  
   ```sh
   python chatbot.py
   ```

2. **Chat with Markhor AI**:  
   ```
   Hi there! I am Markhor, the AI chatbot powered by ChatGPT-4, represented by Coding Moves.
   How can I assist you today?

   You: Hello!
   Markhor AI: Hi! How can I help you today?
   ```

3. **Exit the chat** by typing: `"exit"`, `"quit"`, or `"bye"`.

---

## 📌 Example Code  

```python
import requests
from config import API_KEY  # Secure API key handling

API_URL = "https://api.openai.com/v1/chat/completions"

def chat_with_ai(user_message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post(API_URL, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"] if response.status_code == 200 else "Error occurred!"

# Run chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Markhor AI: Goodbye!")
        break
    print("Markhor AI:", chat_with_ai(user_input))
```

---

## 🚀 How to Contribute  

🔹 Fork the repository  
🔹 Create a new branch (`git checkout -b feature-branch`)  
🔹 Make changes and commit (`git commit -m "Added new feature"`)  
🔹 Push to the branch (`git push origin feature-branch`)  
🔹 Open a **Pull Request**  

Contributions are welcome! Feel free to improve and enhance the chatbot.

---

## 📝 License  

This project is open-source and available under the **MIT License**.

---

## 💡 Developed By  

👨‍💻 **Muawiya**  
🔗 [GitHub](https://github.com/Muawiya-contact)  
📢 **Powered by Coding Moves**  

---

## 🎯 Support  

⭐ **Star** this repository if you found it helpful!   
📢 Share it with others!   
💬 Feel free to open an **issue** for suggestions or bugs!  

---

**Happy Coding! 🚀🤖**
