import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# Speech to Text
# -----------------------------
def speech_to_text(audio_path: str) -> str:
    """
    Converts audio speech to text using OpenAI Whisper.
    """
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript

# -----------------------------
# Text to Speech
# -----------------------------
def text_to_speech(input_text: str, output_path: str = "temp_audio/response.mp3") -> str:
    """
    Converts text to speech using OpenAI TTS.
    Saves the result as an MP3 file.
    """
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=input_text
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    response.stream_to_file(output_path)
    return output_path

# -----------------------------
# Generate Chatbot Answer
# -----------------------------
def get_answer(messages: list) -> str:
    """
    Generates chatbot reply using OpenAI GPT.
    """
    system_message = [{"role": "system", "content": "You are a helpful AI assistant."}]
    messages = system_message + messages
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

# -----------------------------
# Convert Audio to Base64
# -----------------------------
def audio_to_base64(file_path: str) -> str:
    """
    Converts audio file to base64 string (useful for web embedding).
    """
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode()
