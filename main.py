import os
import webbrowser
import datetime
import wikipedia
import pywhatkit
import pyjokes
import pyautogui
import psutil
import openai
import speech_recognition as sr
import pyttsx3

# ——— CONFIG ———
openai.api_key = "YOUR_OPENAI_API_KEY"  # Add your key here

# ——— VOICE SETUP ———
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except:
        return ""


def ask_chatgpt(prompt):
    try:
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        speak(resp.choices[0].text.strip())
    except Exception as e:
        speak("ChatGPT failed to respond.")
        print("OpenAI error:", e)

def run_jarvis():
    speak("Welcome! I am Jarvis, created by Sourabh .")

    while True:
        cmd = take_command()
        if not cmd:
            continue

        if 'who are you' in cmd or 'your creator' in cmd:
            speak("I was created by Sourabh, a skilled software developer from India.")

        elif 'who is sourabh' in cmd:
            speak("Sourabh is a passionate developer, working on futuristic AI technologies.")

        elif 'time' in cmd:
            now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {now}")

        elif 'date' in cmd or 'day' in cmd:
            today = datetime.datetime.now().strftime('%A, %d %B %Y')
            speak(f"Today is {today}")

        elif 'weather' in cmd:
            webbrowser.open("https://www.google.com/search?q=weather")

        elif 'news' in cmd:
            speak("Opening latest news.")
            webbrowser.open("https://news.google.com")

        elif 'battery' in cmd:
            battery = psutil.sensors_battery()
            speak(f"Battery is at {battery.percent}%")

        elif 'screenshot' in cmd:
            pyautogui.screenshot().save("screenshot.png")
            speak("Screenshot saved.")

        elif 'wikipedia' in cmd:
            topic = cmd.replace("wikipedia", "").strip()
            try:
                info = wikipedia.summary(topic, sentences=2)
                speak(info)
            except:
                speak("I couldn't find that topic.")

        # Socials
        elif 'open instagram' in cmd:
            webbrowser.open("https://instagram.com/YOUR_USERNAME")
        elif 'open facebook' in cmd:
            webbrowser.open("https://facebook.com/YOUR_USERNAME")

        # Music
        elif 'play arijit' in cmd:
            pywhatkit.playonyt("Arijit Singh songs")
        elif 'play honey singh' in cmd:
            pywhatkit.playonyt("Honey Singh songs")
        elif 'play kk' in cmd:
            pywhatkit.playonyt("KK best songs")
        elif 'play atif' in cmd:
            pywhatkit.playonyt("Atif Aslam songs")
        elif 'play love song' in cmd:
            pywhatkit.playonyt("Hindi romantic love songs")
        elif 'play motivational song' in cmd:
            pywhatkit.playonyt("Motivational Hindi songs")
        elif 'play mind relax song' in cmd:
            pywhatkit.playonyt("Relaxing music")

        elif 'open youtube' in cmd:
            webbrowser.open("https://youtube.com")
        elif 'open google' in cmd:
            webbrowser.open("https://google.com")

        elif 'chatgpt' in cmd or 'ask' in cmd:
            speak("What would you like to ask?")
            question = take_command()
            if question:
                ask_chatgpt(question)

        elif 'cricket' in cmd:
            speak("Fetching latest cricket updates.")
            webbrowser.open("https://www.cricbuzz.com/")

        elif 'exit' in cmd or 'stop' in cmd:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    run_jarvis()
