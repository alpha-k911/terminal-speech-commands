import speech_recognition as sr
import pyaudio
import os
r = sr.Recognizer()

#with noalsaerr() as n, Microphone() as source:
with sr.Microphone() as source:
    print("Say something that i can recognize: ")
    audio = r.listen(source)
    try:
        print("[+] Listening...."+"\n")
        text = r.recognize_google(audio)
        print("I guess {}".format(text))
        if text=="Alpha":
            os.system("gnome-screensaver-command -l")
    except:
        print("I didn't get")

