#i have installed few modules such as speech recognition,datetime,pyttsx3(text to speech conversion library in python)
#wikipedia,webbrowser,etc.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib #to send mail from gmail using this program we have to change the setting of gmail to "lesser secure app".


engine=pyttsx3.init("sapi5") ##sapi5 is windows inbuilt voice
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morining!")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good  evening")
    speak("I am   jarvis   at   your  service  sir  ")


def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1#it will gives some time to complete the sentence
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said::", query)

    except Exception as e:
        #print(e) #this will print the error ,no need to write this statement
        print("say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'yourpassword-here')
    server.sendmail('yourmail@gmial.com' ,to , content)
    server.close()



if __name__  ==  "__main__":
    wishMe()
    while True:#to run the program infinite times
    #if 1:#to run the program once

        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\suraj singh\\Documents\\jarvis music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif "the time " in query:
            t1= datetime.datetime.now().strftime("%H:%M:%S")#we also use different formats of date
            speak(f"the time is {t1}")
            print(t1)

        elif "the date" in query:
            d1= datetime.datetime.now().strftime("%d:%m:%Y")
            speak(f"the date is {d1}")
            print(d1)
            #d2=datetime.datetime.now().strftime("%B %d %Y")#%B is used to get full name of month
            #print(d2)
            #speak(d2)
            #d3=datetime.datetime.now().strftime("%b %d %Y")#%b is used get half name of month
            #print(d3)
            #speak(d3)

        elif "open code" in query:
            codepath = "C:\\Users\\suraj singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif "email to suraj" in query:
            try:
                speak("what would I say?")
                content= takeCommand()
                to= 'yourmail@gmaol.com'
                sendEmail(to, content)
                speak("email has been sent!!")

            except Exception as e:
                print(e)
                speak("sorry my friend sooraj .I am not able to send your email")



        elif "quit" in query:
            exit()

