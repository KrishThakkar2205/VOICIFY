import speech_recognition as sr
import googletrans as trans
import gtts as ts
import playsound as ps
import os
import pyttsx3 as ps1

engine = ps1.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
spoken_lang, translated_lang = '', ''

audiopath = os.path.join("Audios", "audio.mp3")


#taking the language input
def languageInput():
    with sr.Microphone() as mic:
        global spoken_lang, translated_lang
        engine.say("Enter the language you are speaking : ")
        engine.runAndWait()
        try:
            print("Enter the language you are speaking : ", end="")
            lang = recognizer.listen(mic,timeout=5, phrase_time_limit=5)

            spoken_lang = recognizer.recognize_google(lang).lower()
            print(spoken_lang)

            engine.say("Enter the language you want to translate your text in : ")
            engine.runAndWait()
            print("Enter the language you want to translate your text in : ",end="")
            lang = recognizer.listen(mic,timeout=5, phrase_time_limit=5)
            translated_lang = recognizer.recognize_google(lang).lower()
            print(translated_lang)
        except Exception as e:
            engine.say(
                "A fatal error has been occurred. We regret the interruption!!"
            )
            engine.runAndWait()
            return

    for key, value in trans.LANGUAGES.items():
        if (value == translated_lang):
            translated_lang = key
        elif (value == spoken_lang):
            spoken_lang = key


#exit phrase matching
def findExit(text):
    keywords = ["exit", "quit", "terminate", "end", "stop"]
    for i in text.split():
        if i in keywords:
            return True
    return False


#translating the sentences
def translate():
    global spoken_lang, translated_lang
    engine.say("Welcome to Translation model!")
    engine.runAndWait()
    languageInput()
    if spoken_lang == '' or translated_lang == '':
        return
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Speak now : ")
            voice = recognizer.listen(mic, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(voice, language=spoken_lang)
        try:
            translator = trans.Translator()
            translation = translator.translate(text, dest=translated_lang)
            if findExit(text) or findExit(translation.text):
                engine.say("Thank you! This is Translation model. You are now exiting it!")
                engine.runAndWait()
                break
        except Exception as e:
            engine.say("A fatal error has been occurred. We regret the interruption!!")
            engine.runAndWait()
            return
        converted = ts.gTTS(translation.text, lang=translated_lang)
        converted.save(audiopath)
        ps.playsound(audiopath)
        os.remove(audiopath)