# main.py
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from faq_bot import get_response

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        query = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {query}")
        return query
    except sr.UnknownValueError:
        return "I couldn't understand that."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

def speak(text):
    print(f"🤖 Bot: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def chat_loop():
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye!")
            break
        response = get_response(user_input)
        speak(response)

if __name__ == "__main__":
    chat_loop()