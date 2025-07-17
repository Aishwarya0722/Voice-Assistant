
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def run_assistant():
    speak("Hello! How can I help you?")
    while True:
        command = get_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")
        elif "date" in command:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {date}")
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        elif "search" in command:
            query = command.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        elif command != "":
            speak("Sorry, I can’t do that yet.")

run_assistant()
