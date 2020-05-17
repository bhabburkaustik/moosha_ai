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
import tkinter as tk 
from PIL import Image
import subprocess
import os
import time
import sys
from PIL import Image, ImageTk
import pyautogui
from sclib import SoundcloudAPI, Track, Playlist
import threading
import imageio

#root = tkinter.Tk()
#inname ="tenor.gif"
#root.mainloop()

class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass
        
        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)
        
    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)
        
    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)
        
    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)





def userstart():
    print("enter your name")
    speak("sir pls enter your name")
          


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe(user):
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
    
    
def data():
    data_source = 'kaggle' # alphavantage or kaggle

    if data_source == 'alphavantage':
        # ====================== Loading Data from Alpha Vantage ==================================

        api_key = '<OCE7PAUAGN24EUHE>'

        # American Airlines stock market prices
        ticker = "AAL"

        # JSON file with all the stock market data for AAL from the last 20 years
        url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)

        # Save data to this file
        file_to_save = 'stock_market_data-%s.csv'%ticker

        # If you haven't already saved data,
        # Go ahead and grab the data from the url
        # And store date, low, high, volume, close, open values to a Pandas DataFrame
        if not os.path.exists(file_to_save):
            with urllib.request.urlopen(url_string) as url:
                data = json.loads(url.read().decode())
                # extract stock market data
                data = data['Time Series (Daily)']
                df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
                for k,v in data.items():
                    date = dt.datetime.strptime(k, '%Y-%m-%d')
                    data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                                float(v['4. close']),float(v['1. open'])]
                    df.loc[-1,:] = data_row
                    df.index = df.index + 1
            print('Data saved to : %s'%file_to_save)        
            df.to_csv(file_to_save)

        # If the data is already there, just load it from the CSV
        else:
            print('File already exists. Loading data from CSV')
            df = pd.read_csv(file_to_save)

    else:

        # ====================== Loading Data from Kaggle ==================================
        # You will be using HP's data. Feel free to experiment with other data.
        # But while doing so, be careful to have a large enough dataset and also pay attention to the data normalization
        df = pd.read_csv(os.path.join('Stocks','hpq.us.txt'),delimiter=',',usecols=['Date','Open','High','Low','Close'])
        print('Loaded data from the Kaggle repository')
        
        
        df = df.sort_values('Date')

# Double check the result
        df.head()
        
    
   

def speakCommand(user):
    if __name__ == "__main__":
        wishMe(user)
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
                
                
            elif 'write in notepad' in query:
                
                notepadpath = "%windir%\system32\notepad.exe"
                os.startfile(notepadpath)
                engine = pyttsx3.init() 
                engine.say(command)             
                engine.runAndWait()
                speak('name your file')
                input()
                f= open(user18+".txt","w+")
                speak('your file craeted')
                f.write = write()
                    
                
                
            elif 'play music' in query:
            
                api = SoundcloudAPI()  # never pass a Soundcloud client ID that did not come from this library

                track = api.resolve('https://soundcloud.com/itsmeneedle/sunday-morning')

                assert type(track) is Track

                filename = f'./{track.artist} - {track.title}.mp3'

                with open(filename, 'wb+') as fp:
                
                    track.write_mp3_to(fp)

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
                
                client = wolframalpha.Client('TA5L4V-KPPGYA6GE4') 
      
                indx = query.split().index('calculate') 
                query = query.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text 
                speak("The answer is " + answer) 
                
                
            elif 'show data' in query:
            
               speak(data())
               
                
               
                
            
            
            elif 'close' in query:
                speak("see you soon " + user)
                exit()
            
            else :
                webbrowser.open(query)
            
            

#print("enter your name")   
#user = input()    
user = "kaustik"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)         

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)

    
def closeApp():
    root.destroy()
    exit()

def getName ():  
    user = entry1.get()
    label1 = tk.Label(root, text= user)
    mylabel = tk.Label(text = user)
    mylabel.pack()
    x = threading.Thread(target=speakCommand, args=(user,), daemon=True)
    x.start()

        
button1 = tk.Button(text='Enter Name', command=getName)
canvas1.create_window(200, 180, window=button1)
canvas1.pack()


#for filename in filenames:
    #images.append(imageio.imread(filename))
#imageio.mimsave('/path/to/movie.gif', images)

image = Image.open("C:\\Users\\kaustik\\Downloads\\loader-ai-siri_2x.gif")
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo)
label.pack()

#frames = [PhotoImage(file='loader-ai-siri_2x.gif',format = 'gif -index %i' %(i)) for i in range(100)]

#label = Label(root)
#label.pack()
#root.after(0, update, 0)

button1 = tk.Button(text='Exit', command=closeApp)
button1.pack()

root.mainloop()
