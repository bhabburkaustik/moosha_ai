# moosha_ai
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning kaustik")
    elif hour>=12 and hour<4:
        speak("Good afternoon kaustik")
    else:
        speak("Good Evening kaustik")

        speak("I am your Assistant moosha")
    
        
    
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
        speak("Sorry kaustik, can you repeat that again?")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhabburkaustik@gmail.com', 'Kaustik123')
    server.sendmail('sarika.bhabbur1@gmail.com',to, content)
    server.close()
def process_text(input): 
    try: 
        if 'search' in input or 'play' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
  
        elif "who are you" in input or "define yourself" in input: 
            speak = '''Hello, I am Person. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak) 
            return
  
        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by Sheetansh Kumar."
            assistant_speaks(speak) 
            return
  
        elif "geeksforgeeks" in input:# just 
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            assistant_speaks(speak) 
            return
  
        elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistant_speaks("The answer is " + answer) 
            return
  
        elif 'open' in input: 
              
            # another function to open  
            # different application availaible 
            open_application(input.lower())  
            return
  
        else: 
  
            assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    except : 
  
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input)

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
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
        elif 'email' or 'gmail' in command:
            speak('What is the subject?')
            time.sleep(3)
            subject = myCommand()
            speak('What should I say?')
            time.sleep(3)
            message = myCommand()
            content = 'Subject: {}\n\n{}'.format(subject, message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        #identify to server
        mail.ehlo()

        #encrypt session
        mail.starttls()

        #login
        mail.login('bhabburkaustik@gmail.com', 'Kaustik123')

        #send message
        mail.sendmail('FROM', 'TO', content)

        #end mail connection
        mail.close()

        talk('Email sent.')
        
        elif 'close' in query:
            speak("see you soon kaustik")
            exit()
        
        else :
            webbrowser.open(query)
