import speech_recognition as sr
import pyttsx3 as ps
import SpeechRecognition as srn
import Translation as translate
import Automation as automate

recognizer = sr.Recognizer()
engine = ps.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Welcome to Voicify!!")
engine.runAndWait()



while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("1. Speech To Text Transcript generator!")
        print("2. Translation with Transcript Model!")
        print("3. Automation Model")
        print("4. Exit")
        engine.say("Please input your option in form of numbers only!")
        engine.runAndWait()
        audio = recognizer.listen(mic, timeout=5, phrase_time_limit=5)
        print("Recognizing..")
        try:
            text = recognizer.recognize_google(audio)
        except Exception as e:
            engine.say("Command not understood, please say a command!")
            engine.runAndWait()
            continue

        if "one" in text or "1" in text or "first" in text:
            print("")
            srn.startSpeech()
            print("")
        elif "two" in text or "2" in text or "second" in text:
            print("")
            translate.translate()
            print("")
        elif "three" in text or "3" in text or "third" in text:
            print("")
            automate.main()
            print("")
        elif "four" in text or "4" in text or "fourth" in text:
            print("")
            engine.say("Thank you for this awesome journey! I hope that your journey has been well. Thank you so much! This is VOICIFY and you were having fun with Voicify")
            engine.runAndWait()
            break
        else:
            print("")
            engine.say("The entered option is invalid. Please select a valid option")
            engine.runAndWait()
            print("")
