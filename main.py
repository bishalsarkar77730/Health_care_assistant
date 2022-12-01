from pygame import mixer
import datetime
import pyttsx3
import time

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 150)

file = 'D:\\music\\water.mp3'
file2 = 'D:\\music\\meep_meep.mp3'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your Health Care assistant. I will always take care of You, dont worry, Do Your Work With Perfection")


wishMe()
speak("after Every 30 min you have to drink water and after Every 1 Hour You have to take 5 - 10 min rest")


def healthy():
    while 'true':
        time.sleep(1800)

        mixer.init()
        mixer.music.load(file)
        mixer.music.set_volume(0.9)
        mixer.music.play(-1)
        print("Type S to stop")
        query = input(" ")
        if query == 's':
            mixer.music.stop()
            print("you drinks your water")
        else:
            mixer.music.play()
            print("wrong input try again")
        time.sleep(3600)
        mixer.init()
        mixer.music.load(file2)
        mixer.music.set_volume(0.9)
        mixer.music.play(-1)
        print("Type 5 For 5 min Rest or Type 10 for 10 min Rest")
        user = input(" ")
        if user == '5':
            mixer.music.stop()
            speak("Your Five Minutes Break starts Enjoy Your Five Minutes")
            time.sleep(300)
            speak("Your Five minutes of rest is finished get Back to work")
        elif user == '10':
            mixer.music.stop()
            speak("Your Ten Minutes Break starts Enjoy Your Ten Minutes")
            time.sleep(600)
            speak("Your Ten minutes of rest is finished get Back to work")
        else:
            mixer.music.play()
            speak("wrong input try again")
        break
    again()


def again():
    speak("do you want to do it again Say YES Or NO")
    print("type y or n")
    while True:
        query = input(" ")

        if 'y' in query:
            healthy()
        elif 'n' in query:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour < 12:
                speak("Bye, Have A Good Day")
            elif 12 <= hour < 18:
                speak("Bye, Have a Good Noon")
            else:
                speak("Bye, Sir Good Night, Have a Beautiful Night")
        else:
            break


healthy()
