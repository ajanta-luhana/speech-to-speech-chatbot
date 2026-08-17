from speech_chatbot.chatbot import get_answer

messages = [
    {"role": "user", "content": "Say hello in one short sentence."}
]

response = get_answer(messages)

print("AI Response:")
print(response)