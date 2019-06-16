import speech_recognition as sr
import pyaudio
import os
import time

# from sqlalchemy import true

r = sr.Recognizer()

#with noalsaerr() as n, Microphone() as source:
with sr.Microphone() as source:
    while True:
        time.sleep(2)
        print("Say something that i can recognize: ")
        audio = r.listen(source)
        try:
            print("[+] Listening...."+"\n")
            text = r.recognize_google(audio)
            print("I guess {}".format(text))
            if text.__contains__("Alpha"):
                os.system("gnome-screensaver-command -l")
        except:
            print("I didn't get")