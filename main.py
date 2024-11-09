import os
import subprocess
import speech_recognition as sr
import webbrowser
import datetime


import os

def say(text):
    subprocess.run(['PowerShell', '-Command', f"Add-Type -AssemblyName 'System.Speech'; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"])

def close_browser_tabs():
    if os.name == 'nt':  # For Windows
        os.system("taskkill /IM chrome.exe /F")

def takeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 0.6
            print("Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}")
                return query
            except sr.UnknownValueError:
                say("Sorry, I did not understand that.")
                return "Sorry, I did not understand that."
            except sr.RequestError:
                say("Sorry, my speech service is down.")
                return "Sorry, my speech service is down."
    except Exception as e:
        print(f"Error: {e}")
        return "Microphone not available."

if __name__ == '__main__':
    say("hello Harsh, I am Jarvis A I!!")
    while True:
        query = takeCommand()
        if query:
            sites = [
                ["youtube", "https://www.youtube.com"],
                ["wikipedia", "https://www.wikipedia.com"],
                ["google", "https://www.google.com"],
                ["instagram", "https://www.instagram.com"]
            ]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]}, sir....")
                    webbrowser.open_new_tab(site[1])
                    break
            else:
                if "open music" in query.lower():
                    musicPath = "C:\\Users\\boyr2\\Downloads\\O-Mere-Dil-Ke-Chayan.mp3"
                    os.system(f'start {musicPath}')  # Using 'start' for Windows
                elif "the time" in query.lower():
                    hour = datetime.datetime.now().strftime("%H")
                    minute = datetime.datetime.now().strftime("%M")
                    say(f"Sir, the time is {hour} hours and {minute} minutes.")
                elif "open camera" in query.lower():
                    say("Opening camera")
                    os.system("start microsoft.windows.camera:")
                elif "open whatsapp" in query.lower():
                    os.system("start whatsapp:")
                # elif "using ai" in query.lower():
                #     ai(query)
                elif "close all tabs" in query.lower():
                    say("Closing all tabs")
                    close_browser_tabs()
                elif "shutdown" in query.lower():
                        os.system("shutdown /s /t 1")
                elif "harsh" in query.lower():
                    say("Shaily ji harsh tumhe like karta hai  ")