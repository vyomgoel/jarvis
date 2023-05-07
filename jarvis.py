import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


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
  
    if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
            
        elif 'open google' in query:
                webbrowser.open("google.com")
                
        elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                
                
        elif 'play music' in query:
                webbrowser.open("https://open.spotify.com/playlist/7DYwD8wnBFnvXBsVP0NEtM")
                 
        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            
        elif 'open vs code' in query:
                codepath = "C:\\Users\\vyomt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                
        elif 'open vs code' in query:
                codepath = "C:\\Users\\vyomt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                
        elif 'email to vyom' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vyomyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")    

            
            
      
      
      
      
    
    