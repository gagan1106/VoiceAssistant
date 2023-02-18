import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
import time
import pyautogui


engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)#for female voice - voices[1].id


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello sir. I am your Virtual Assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'my name' in query:
            speak('your name is Gagan')
        
        elif 'my age' in query:
            speak('your age is 18')
        
        elif 'my college' in query:
            speak('your college name is Noida Institute of Engineering and Technology situated in Greater Noida')
            
        elif 'who are you' in query:
            speak('Sir, I am the kind of assistant that has plenty of energy and never gets tired, How can i help you ')
            
        elif 'how are you' in query:
            speak("I am fine Sir")
        
        elif 'describe yourself' in query:
            speak('I am the kind of assistant created by Gagan by using python programming language. In creation of me' 
                  'different types of python library was used like pyttsx3,speech recognition, webbrowser, wikipedia,' 
                  'date time etc, pyttsx3 is used to text-to-speech conversion. speech recognition, the ability of devices'
                  'to respond to spoken commands. webbrowser module is a convenient web browser controller. It provides a'
                  'high-level interface that allows displaying Web-based documents to users.  Pyjokes library that is used'
                  'to create one-line jokes for programmers. Datetime module supplies classes to work with date and time. '
                  'smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet'
                  ' machine with an SMTP or ESMTP listener daemon.Wikipedia is a Python library that makes it easy to access'
                  ' and parse data from Wikipedia.')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'college cloud' in query:
            webbrowser.open("niet.instituteoncloud.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open('web.whatsapp.com')

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\my files\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
       
        elif 'tell me date' in query:
            date=datetime.datetime.now().strftime("%D %d %Y") 
            speak(f"The Current date is {date}")

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\vscode programs"
            os.startfile(codePath)
       
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop  from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')
            
        elif 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'thank you' in query or "thanks" in query:
            speak("It's my pleasure., sir")
        elif 'exit' in query:
            speak("Thanks for giving me your time Good bye!,Have a nice day")
            break
        

        