from logging import exception
import sys
from time import sleep
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
from bs4 import BeautifulSoup
import keyboard
from playsound import playsound
import os
import pyautogui
import requests
import smtplib
import pyjokes
from plyer import notification
from wikipedia.exceptions import DisambiguationError, PageError

from toolS import make_request, sendEmail, takeCommand, wishMe


name_of_ai = "zira"


from toolS import speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    def make_request(url):
        response = requests.get(url)
        return response.text


#################################### MAIN COMMANDS ####################################
def mainBackend():
    wishMe(name_of_ai)
    while True:
    # if 1:
        query = takeCommand().lower()
        #query = input('Commands?')

        # Logic for executing tasks based on query
        if query == "":
            speak("Speak something.")

        #################################### EMOTIONS ####################################
        elif 'hello' in query:
            speak(f"I Am {name_of_ai} .")
            speak("Welcome Dimple and Deepika ma'am to virtual world.")
            speak("Your Personal AI Assistant!")
            speak("How May I Help You?")

        elif 'how are you' in query:
            speak("I Am Fine Sir!")
            speak("Whats About YOU?")

        #################################### BREAK TIME ####################################
        elif 'you need a break' in query:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak(f"Just Say Wake Up {name_of_ai}!")
            break


        #################################### WIKIPEDIA ####################################
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=1, auto_suggest=False)
                speak("According to Wikipedia")
                print(results)
                notification_message = f"{results}"
                notification.notify(
                    title=f"Search Results for {query}",
                    message=notification_message,
                    timeout=5
                )
                speak(results)
            except PageError as pg:
                notification_message = f"{query.capitalize()} Not Found"
                notification.notify(
                    title=f"Search Results for {query}",
                    message=notification_message,
                    timeout=5
                )
                speak(f"{query} not found.")
            except DisambiguationError as pg:
                notification_message = f"{query.capitalize()} Not Found"
                notification.notify(
                    title=f"Search Results for {query}",
                    message=notification_message,
                    timeout=5
                )
                speak(f"{query} not found.")
                

        #################################### CHROME TOOLS ####################################
        
        elif 'open facebook' in query:
            from openApps import OpenApps
            OpenApps(query)

        elif 'open instagram' in query:
            from openApps import OpenApps
            OpenApps(query)

        elif 'open whatsapp' in query:
            from openApps import OpenApps
            OpenApps(query)

        elif 'open maps' in query:
            from openApps import OpenApps
            OpenApps(query)

        elif 'open code' in query:
            from openApps import OpenApps
            OpenApps(query)

        elif 'open youtube' in query:
            from openApps import OpenApps
            OpenApps(query)
            
        elif 'open telegram' in query:
            from openApps import OpenApps
            OpenApps(query)

        elif 'open chrome' in query:
            from openApps import OpenApps
            OpenApps(query)   
        
        elif 'chrome tool' in query:
            from toolS import ChromeTools
            ChromeTools()

        elif 'youtube tool' in query:
            from toolS import YoutubeTools
            YoutubeTools(name_of_ai)

        elif 'whatsapp tool' in query:
            from toolS import WhatsAppTools
            WhatsAppTools(name_of_ai)



        elif 'repeat my word' in query:
            speak("Speak Sir!")
            jj = takeCommand()
            speak(f"You Said : {jj}")


        elif 'my location' in query:
            speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@30.6033574,76.8498397,16z')
        
        
        #################################### OPEN WEBSITE ####################################
        elif 'open website' in query:
            speak(
                "Please speak the name of the website that you want to open (specify the full url) \n")
            website_name = takeCommand()
            print(website_name)
            webbrowser.open(website_name)
            speak(f"https://{website_name} opened.")

        
        #################################### PLAY MUSIC ####################################
        elif 'play music' in query:
            music_dir = 'E:\\song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        
        #################################### TIME ####################################
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("'%I:%M %p'-")    
            speak(f"Sir, the time is {strTime}")

        #################################### OPEN VSCODE ####################################
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        #################################### SEND EMAIL ####################################
        elif 'email' in query:
            try:
                speak("to whom")
                to = takeCommand().lower()
                to = to.replace(' ', '')
                print(to)
                to = (f"{to} @gmail.com")
                print(to)

                speak("What should I say?")
                content = takeCommand()
                print(content)
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")  

        
        
        #################################### JOKE ####################################
        elif "joke" in query:
            speak(pyjokes.get_joke())

        
        elif "introduce yourself" in query:
            speak("Okay,Let me start by The time I was born,,")
            speak("I was a dream of a boy dreaming to make a perfect virtual assistant")
            speak("He soon established the company named sachin n a l l e e")
            speak("Slowly,I came to life")
            speak("I started learning various things like calculations,General knowldge etc etc")
            speak("Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
            speak("Okay,thats a wrap I wont say more ")

        #################################### WINDOW FEATURES ####################################
        elif 'take me to desktop' in query:
            keyboard.press_and_release('windows + d')
        
        elif 'open file explorer' in query:
            keyboard.press_and_release('windows + e')


        #################################### ZOOM CLASSES ####################################
        elif 'open zoom' in query:
            from toolS import ZoomTools
            ZoomTools()

            

        #################################### TAKE SCREENSHOT ####################################
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')

        #################################### SEARCH SOMETHING ####################################
        elif 'search' in query:
            speak("What do you want me to search for (please speak) ? ")
            search_term = takeCommand()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(search_url)
            speak(f"here are the results for the search term: {search_term}")

        #################################### COVID STATS ####################################
        elif 'covid stats' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
                title="COVID-19 Statistics",
                message=notification_message,
                timeout=5
            )
            speak("here are the stats for COVID-19")
        #################################### I QUIT ####################################
        elif "quit" in query:
            speak("I'm ultron. Speed 1 terahertz, memory 1 zigabyte shutting down")
            sys.exit()
        # else:
        #     speak("I didn't understand.")
        



        #################################### END OF THE PROGRAM ####################################