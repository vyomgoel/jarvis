import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from AppOpener import open
import subprocess

local_path = 'C:\\Users\\vyomt'

# an intallation to take in voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir ")

    else:
        speak("Good evening sir ")
    speak(" I am Jarvis. Please tell me how may i help you")
        
def takeCommand():
    # It takes microphonr input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
        
if __name__ == "__main__":
    wishMe()
  
    while True:
        query = takeCommand().lower() #Converting user query into lower case

        # WIKIPEDIA
        
        # Logic for executing tasks based on query
        if query.startswith('wikipedia'):  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        # SEARCH GOOGLE        
                
        elif  query.startswith("google"):
                webbrowser.open(f"www.google.com/search?q={query.replace('google', '')}")
        
        # OPEN ANY INSTALLED APP 
             
        elif  query.startswith("open app"):
                open(query.replace('open app', '').upper())
        
        # OPEN ANY FOLDER
        
        elif  query.startswith("open folder"):
            subprocess.Popen(f'explorer /root,"search-ms:query={query.replace("open folder", "")}&crumb=folder:{local_path}&"')
            
        # OPEN YOUTUBE
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        # OPEN STACKOVERFLOW    
              
        elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                
        # PLAY MUSIC
        
        elif 'play music' in query:
                webbrowser.open("https://open.spotify.com/playlist/7DYwD8wnBFnvXBsVP0NEtM")
                
        # CURRENT TIME
               
        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M")    
                speak(f"Sir, the time is {strTime}")
  


        
       
                
        
                
        
            
            
      
      
      
      
    
    