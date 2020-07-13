import pyttsx3
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Mitangshu ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Mitangshu")

    else:
        speak("Good Evening Mitangshu")
    speak(" I am Sarah. Please tell me how can i assist You ")

def Commands():
    '''

    takes command fro the user as string and return an output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        #r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print(" Can you please repeat your query....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mitangshu11@gmail.com', 'football11')
    server.sendmail('mitangshu11@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    Greetings()


    query =Commands().lower()
        # logic for executing tasks based on query
    while True:
        if 'wikipedia' in query:
            speak("Searching in wikipedia..... ")
            query = query.replace('wikipedia', '')
            results= wikipedia.summary(query,sentences = 2)
            speak('Accorfing to Wikipedia')
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    
        elif 'open google' in query:
            webbrowser.open("google.com")
    
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
    
    
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
    
        elif 'email to Me' in query:
            try:
                speak("What should I say?")
                content = Commands()
                to = "mitangshu11@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry not able to send this email")
        
