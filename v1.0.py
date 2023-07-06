import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import AppOpener
import pywhatkit
import random
import keyboard
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    speak("Now me to introduce myself, I am ADVIKA  ,a virtual Assistant, i am here to assist you in variety of tasks as best as i can.")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing......")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query

def features():

    def telltime():
         hour = int(datetime.datetime.now().hour)
         minute = int(datetime.datetime.now().minute)
         if hour < 12:
             return ("Good morning it's %d %d" % (hour, minute))

         elif hour >= 12 and hour < 16:
             return ("Good afternoon it's %d %d" % (hour, minute))

         else:
             return ("Good evening it's %d %d" % (hour, minute))

   

    def tran():
         speak("Tell me the line, sir!")
         line = takeCommand_hindi()
         traslate = Translator()
         result= traslate.translate(line)
         Text = result.text
         speak(Text)
    

    def YTauto():
        speak("What's your command ?")
        query = takeCommand()
        
        if 'pause' in query:
            keyboard.press('space bar')
        
        if 'play' in query:
            keyboard.press('space bar')
    
        elif 'restart' in query:
            keyboard.press('0')
        
        elif 'mute' in query:
            keyboard.press('m')

        elif 'unmute' in query:
            keyboard.press('m')
         
        elif 'skip' in query:
            keyboard.press('1 ')

        elif 'back' in query:
            keyboard.press('j ')
         
        elif 'full screen' in query:
            keyboard.press('f')
        
        elif ' film mode' in query:
            keyboard.press('t')
    
    def CloseApp():
        speak("ok sir, wait a second")
        
        if 'youtube' in query:
            os.system("TASKKILL /F /im msedge.exe")

        if 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        if 'whatsapp' in query:
            os.system("TASKKILL /F /im whatsapp.exe")
        
        if 'file explorer' in query:
            os.system("TASKKILL /F /im fileexplorer.exe")

        if 'vs code' in query:
            os.system("TASKKILL /F /im code.exe ")

    def OpenSong():
        speak("What you want to play")
        songname = takeCommand()
        
        if 'kesariya' in songname:
            os.startfile('C:\\  Users\\UP43R\\Downloads\\Music\\kesariya')
        elif '        ' in query:
            speak('I am sure you will like this song')
            pywhatkit.playonyt('arijitsingh')
        else:
            pywhatkit.playonyt(songname)

    def OpenWeb():
        speak("which website ,sir")
        web = takeCommand()
        web = web.replace("website","")
        web = web.replace("advika","")
        web = web.replace(" ","")
        search = "https://www." + web +".com"
        speak("Opening it ,sir")
        webbrowser.open(search)

    def Whatsapp():

        speak("Tell Me The Name Of The Person!") 
        name= takeCommand()

        if 'Rahul' in name:
             speak("Tell Me The Message!")
             msg = takeCommand()
             speak("Do you want to send message immediately")
             confor = takeCommand()
             if 'yes' in confor:
                 hour= int(datetime.datetime.now().hour)
                 min= int(datetime.datetime.now().minute)+1
                 pywhatkit.sendwhatmsg("+917275882800",msg,hour,min,25)
                 speak("OK Sir,Message is sent !")
             elif 'no' in confor:
                 speak("Tell Me The Message!")
                 msg = takeCommand()
                 speak("Tell Me The Time Sir!")
                 speak ("Time In Hour!") 
                 hour= int(takeCommand())
                 speak ("Time In Minutes!")
                 min= int(takeCommand())
                 pywhatkit.sendwhatmsg("+917275882800",msg,hour,min,20)
                 speak("OK Sir, Sending Whatsapp Message !")

        elif 'rahul' in name:

             speak("Tell Me The Message!")
             msg = takeCommand()
             speak("Tell Me The Time Sir!")
             speak ("Time In Hour!") 
             hour= int(takeCommand())
             speak ("Time In Minutes!")
             min= int(takeCommand())
             pywhatkit.sendwhatmsg("+917275882800",msg,hour,min+1,20)
             speak("OK Sir, Sending Whatsapp Message !")




    wish = telltime()
    speak(wish + " , I am ADVIKA, Sir" + ", system is active to use")

    while True:
        query = takeCommand().lower()

        #basicOperations
        if 'tell time' in query:
            time_result = telltime()
            speak(time_result)

        elif 'take a break' in query:
            speak("ok sir , call me when you need")
            break

        
        #OpenOperations
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open chrome' in query:
            speak("opening chrome ")
            AppOpener.run("GOOGLE CHROME")

        elif 'open whatsapp' in query:
            speak("OPENING WHATSAPP")
            AppOpener.run("WHATSAPP")

        elif 'open file explorer' in query:
            speak("opening file explorer")
            AppOpener.run("FILE EXPLORER")

        elif 'open vs code' in query:
            speak("opening vs code ")
            AppOpener.run("Visual studio CODE")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)


        #intraction
        elif 'say hello to' in query:
            query = query.replace("say hello to", "")
            speak("hello"+query)

        elif 'repeat' in query:
            query = query.replace("repeat", "")
            speak(query)
        
        elif 'can i change your name' in query:
            query = query.replace("freddie", "")
            query = query.replace("google search", "")
            speak("My name is ADVIKA. I'm sorry,but i can't change what i am. my creators has given me this name and it has heartwarming wishes from them")

        elif 'ok ADVIKA' in query:
            list = ["No problem", "No worries","Dont worry about it", "that's ok"]
            speak(random.choice(list))

        elif 'what is your name' in query:
            speak("My name is ADVIKA ,")

        elif 'who are you' == query:
            intro()

        #Searching
        elif 'youtube search' in query:
            speak("this is what i found sir")
            query = query.replace("freddie", "")
            query = query.replace("youtube search", "")
            search = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(search)

        elif 'google search' in query:
            speak("this is what i found sir")
            query = query.replace("freddie", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
        
        #playsong
        elif 'play song' in query:
            OpenSong() 

        
        elif 'translator' in query:
            tran()

        #youtube control
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'play' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')
        
        elif 'mute' in query:
            keyboard.press('m')

        elif 'unmute' in query:
            keyboard.press('m') 
         
        elif 'skip' in query:
            keyboard.press('1')

        elif 'back' in query:
            keyboard.press('j ')
         
        elif 'full screen' in query:
            keyboard.press('f')
        
        elif 'film mode' in query:
            keyboard.press('t')

        elif 'control youtube' in query:
            YTauto()


        elif 'system shutdown' in query:
            keyboard.press('ctrl+alt+delete')
        
        #reminders
        elif 'remember that' in query:
            msg=query.replace("remember that","")   
            msg=query.replace("ADVIKA ","")    
            rem = open("dataremind.txt","w")
            rem.write(msg)
            rem.close()
        
        elif'what do you remember' in query:
            rem = open("dataremind.txt","r")
            speak("you tell me that"+ rem.read())
        
        #CloseOperations 
        elif 'close youtube' in query:
            CloseApp() 
        
        elif 'chrome' in query:
            CloseApp()

        elif 'close whatsapp' in query:
            CloseApp()
        
        elif 'close file explorer' in query:
            CloseApp()

        elif 'close vs code' in query:
            CloseApp()

        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'open website' in query:
            OpenWeb()
        
        elif 'launch' in query:
            query= query.replace("launch","")
            query= query.replace("advika","")
            search = "https://www." + query.replace(" ","") +".com"
            webbrowser.open(search)
            speak("Opening it sir")

if __name__ =="__main__":
    features()