import random

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# speech to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("how can i help you")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("mehrarenu033@gmail.com","xfhh mejk fthc rvbk")
    server.sendmail("mehrarenu033@gmail.com ",to,content)
    server.close()


if __name__=="__main__":
    # takecommand()
    # speak("hii sir")
    wish()
    while True:
    # if 1:

        query=takecommand().lower()

        # logic building for task

        if "open vscode" in query:
            path="C:\\Users\\mehra\\Downloads\\DOWNLOADS1\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir="C:\\Users\\mehra\\Downloads\\music"
            songs=os.listdir(music_dir)
            # rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "youtube" in query:
            webbrowser.open("youtube.com")
        elif "google" in query:
            speak("what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "send message" in query:
            kit.sendwhatmsg("+919911853757","this is testing protocol",17,10)

        elif "play python" in query:
            kit.playonyt("pythons tutorial")

        elif "send mail to renu" in query:
            try:
                speak("what should i say?")
                content=takecommand().lower()
                to="mehrarenu443@gmail.com"
                sendEmail(to,content)
                speak("email has been sent to renu")
            except Exception as e:
                print(e)
                speak("sorry i m not able to sent msg to renu")

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif"restart system" in query:
            os.system("shutdown /r /t 5")

        elif "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "no thanks" in query:
            speak("Thanks for using me ,have a good day")
            sys.exit()

        elif "ip address" in query:
            speak("well sir, let me check")
        try:
            ipAdd=requests.get("https://api.ipify.org").text
            print(ipAdd)
        except Exception as e:
            print(e)
            pass

        speak("sir do you have any other work")
