import speech_recognition as sr
import pyttsx3
import os
import sys
import subprocess

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

def execute_command(command):
    if "open firefox" in command:
        os.system("start firefox")

    elif "open chat" in command:
        url = "https://chatgpt.com/"
        subprocess.Popen([r"C:/Program Files/Mozilla Firefox/firefox", url])

    elif "close firefox" in command:
        os.system("taskkill /IM firefox.exe /F")

    elif "open youtube" in command:
        url = "https://www.youtube.com/"
        subprocess.Popen([r"C:/Program Files/Mozilla Firefox/firefox", url])

    elif "open reddit" in command:
        url = "https://www.reddit.com/"
        subprocess.Popen([r"C:/Program Files/Mozilla Firefox/firefox", url])

    elif "open pi" in command:
        subprocess.Popen([r"C:/Program Files/JetBrains/PyCharm Community Edition 2024.1.4/bin/pycharm64"])

    elif "open code" in command:
        subprocess.Popen([r"C:/Users/sxxve/AppData/Local/Programs/Microsoft VS Code/Code"])

    elif "open discord" in command:
        speak("Opening Discord")
        subprocess.Popen([r"C:/Users/sxxve/AppData/Local/Discord/Update.exe", "--processStart", "Discord.exe"])

    elif "computer shut down" in command:
        os.system("shutdown /s /t 0")

    elif "computer restart" in command:
        os.system("shutdown /r /t 0")

    elif "exit program" in command:
        speak("Closing the Program")
        sys.exit()

    else:
        speak("Command not recognized")

if __name__ == "__main__":
    while True:
        command = listen_command()
        if command:
            execute_command(command)