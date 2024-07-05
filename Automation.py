import pyautogui
import speech_recognition as sr
import time
import pyttsx3 as ps

engine = ps.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def listen_and_record():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your command : ")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        print("Recognizing...")
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        engine.say("Could not request results from Google Speech Recognition service!")
        engine.runAndWait()
        return None


def process_command(command):
    if "open" in command:
        pyautogui.hotkey("win")
        pyautogui.hotkey("shift", 'home')
        pyautogui.press("backspace")
        pyautogui.write(command[5::])
        pyautogui.press("enter")
        engine.say("Opening " + command[5::])
        engine.runAndWait()

    elif "switch" in command:
        pyautogui.hotkey("alt",'tab')
        # pyautogui.press("enter")
    elif "close" in command:
        engine.say("Closing")
        engine.runAndWait()
        pyautogui.hotkey("alt", "f4")
    elif "search" in command:
        pyautogui.press("/")
        pyautogui.hotkey("shift", 'home')
        pyautogui.press("backspace")
        pyautogui.write(command[6::])
    elif "enter" in command:
        pyautogui.press("enter")
    elif "play" in command:
        engine.say('Playing ' + command[5::])
        engine.runAndWait()
        pyautogui.hotkey("win")
        pyautogui.hotkey("shift", 'home')
        pyautogui.press("backspace")
        pyautogui.write("spotify")
        pyautogui.press("enter")
        time.sleep(10)
        pyautogui.hotkey("ctrl", "k")
        pyautogui.write(command[5::])
        time.sleep(2)
        pyautogui.hotkey("shift", "enter")
    elif "pause" in command or "space" in command:
        pyautogui.press("space")
    elif "minimise" in command:
        pyautogui.hotkey("win", "down")
        pyautogui.hotkey("win", "down")
    elif "left" in command:
        pyautogui.press("left")
    elif "right" in command:
        pyautogui.press("right")
    elif "up" in command:
        pyautogui.press("up")
    elif "down" in command:
        pyautogui.press("down")
    elif "maximize" in command:
        pyautogui.hotkey("win", "tab")



def findExit(text):
    keywords = ["exit", "quit", "terminate", "end", "stop"]
    for i in text.split():
        if i in keywords:
            return True
    return False


def main():
    engine.say(
        "Welcome to the Automation Model! Please select out the commands from the following given list to start!"
    )

    engine.runAndWait()
    print(
        "1. Basic gestures of left, right, up, down -> go to up/down/left/right direction"
    )
    print("2. Open any app -> Open appname")
    print("3. Play song on spotify -> play song name")
    print("4. Close current window -> close this window")
    print("5. search  -> write your message")
    print("6. Minimise current window")
    print("7. Maximise any window -> maximise")
    print("8. Enter and space are direct!")

    while True:
        command = listen_and_record()
        if command and findExit(command):
            engine.say("Thank you! This is Automation model. You are now exiting it!")
            engine.runAndWait()
            break
        if command:
            process_command(command)

