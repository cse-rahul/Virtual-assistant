import speech_recognition as sr
import os

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

while True:

    wakeup = takeCommand()

    if 'wake up' in wakeup:
        os.startfile('C:\\Users\\UP43R\\Desktop\\final MiniProject\\psr\\v1.0.py')
    elif 'hello advika' in wakeup:
        os.startfile('C:\\Users\\UP43R\\Desktop\\final MiniProject\\psr\\v1.0.py')
    else:
        print("Nothing")
