import speech_recognition as sr
import pyttsx3 as ps


def startSpeech():

    engine = ps.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Welcome to Speech to Text model!")
    engine.runAndWait()

    while True:
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as mic:
                print("Please speak :) ")
                # recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic, timeout=5, phrase_time_limit=5)
                print("Translating...")
                text = recognizer.recognize_google(audio)

                if findExit(text):
                    engine.say("Thank you! This is Speech to text model. You are now exiting it!")
                    engine.runAndWait()
                    break
                else:
                    print(text)

        except Exception as e:
            print("Could not understand audio. Please try again.", e)


def findExit(text):
    keywords = ["exit", "quit", "terminate", "end", "stop"]
    for i in text.split():
        if i in keywords:
            return True
    return False
