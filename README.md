# 🎤 Speech-to-Speech Chatbot Module

A simple **speech-to-speech AI chatbot** module built with [OpenAI](https://openai.com/) APIs.  
It takes audio input from a user, converts it to text using **Whisper**, generates a response using **GPT**,  
and converts that response back to speech using **Text-to-Speech**.

This module is **backend-only** — it can be integrated into any frontend (web, desktop, or mobile).  

---

## 🚀 Features
- 🎙 **Speech-to-Text**: Convert spoken words to text via OpenAI Whisper (`whisper-1` model)
- 🤖 **AI Response Generation**: Context-aware chatbot powered by GPT (`gpt-4o-mini`)
- 🔊 **Text-to-Speech**: Convert chatbot responses into natural-sounding speech
- 🛠 **Easy Integration**: Can be used in APIs, automation scripts, or interactive apps

---

## 📂 Project Structure
sts_module/
└── speech_chatbot/
├── init.py # Package initializer
├── chatbot.py # Core speech-to-speech logic
requirements.txt # Python dependencies
.env.example # Example environment variables
README.md # Project documentation

---

## 📦 Installation
1. **Clone the repository**
```bash
git clone https://github.com/AroonKumarr/speech-to-speech-chatbot.git
cd speech-to-speech-chatbot
Create and activate a virtual environment


python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies


pip install -r requirements.txt
Set up environment variables

Copy .env.example to .env



cp .env.example .env
Add your OpenAI API key in .env:



OPENAI_API_KEY=your_api_key_here
🛠 Usage
Example usage inside a Python script:

from sts_module.speech_chatbot.chatbot import speech_to_text, get_answer, text_to_speech

# 1. Convert speech to text
user_text = speech_to_text("input_audio.mp3")

# 2. Get chatbot response
messages = [{"role": "user", "content": user_text}]
bot_reply = get_answer(messages)

# 3. Convert reply to speech
audio_path = text_to_speech(bot_reply)
print(f"Reply saved as: {audio_path}")

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgments
OpenAI for the Whisper, GPT, and TTS APIs

Python community for awesome libraries