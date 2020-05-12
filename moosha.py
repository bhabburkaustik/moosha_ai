import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
from gtts import gTTS
from tkinter import *
from PIL import Image
import subprocess
import os
import sys
from PIL import Image, ImageTk


print("enter your name")

#root = tkinter.Tk()
#inname ="tenor.gif"
#root.mainloop()
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def userstart():
    print("enter your name")
    speak("sir pls enter your name")
          


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
user = input()
def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning!" + user)
        speak ("iam your assistant moosha")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!" + user)
        speak ("iam your assistant moosha")

    elif hour>=18 and hour<24:
        speak("Good Evening !" + user)
        speak ("iam your assistant moosha")

    else:
        speak("Good Night!" + user)
        speak ("iam your assistant moosha")
        
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
   
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
    
        
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry," + user)
        speak("can you repeat that again?")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("music is being played")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\Smartboy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
       
        elif 'open notepad' in query:
            notepadpath = "%windir%\system32\notepad.exe"
            os.startfile(notepad)
            engine = pyttsx3.init() 
            engine.say(command)  
            engine.runAndWait() 
      
         
      
                   
        
            
        elif "who made you"  in query: 
            speak("I have been created by my godfather sir kaustik. who is the greatest computer scientist")
           
            
            
        elif  "define yourself" in query: 
            speak("iam your Assistant hwho makes your work easir and makes you lazy")
            
         
            
        elif  "what is your name" in query: 
            speak("my name is moosha who is also sir kaustik bhabbur's pet sir moosha")
            
            
        elif  "who is pm of india" in query: 
            speak("narendra modi")
            
            
        elif  "what doo you think  about india" in query: 
            speak("what will i think  its my birthplace and my godfather sir kaustik's too..")   
          
        elif "calculate" in query: 
              
            # write your wolframalpha app_id here 
            app_id = "TA5L4V-KPPGYA6GE4" 
            client = wolframalpha.Client('TA5L4V-KPPGYA6GE4') 
  
            indx = query.split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer) 
           
            
        
        
        elif 'close' in query:
            speak("see you soon kaustik")
            exit()
        
        else :
            webbrowser.open(query)
            
