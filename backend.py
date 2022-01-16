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


name_of_ai = "Tokyo"


from toolS import speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    def make_request(url):
        response = requests.get(url)
        return response.text


# #################################### WISH ME ####################################
# def wishMe():
    
#     # speak("Starting Engine")
#     # speak("Collecting required resources")
#     # speak("initializing")
#     # speak("Getting information from the CPU")
#     # speak("contacting with mail services")
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")

         
#     speak(f"I am {name_of_ai} . Give me command")       

# #################################### INPUTING THE VOICE INTO INFORMATION ####################################
# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

# #################################### EMAIL DETAILS ####################################
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('rohitronaldo200@gmail.com', '@Ronaldoisbest123456789')
#     server.sendmail('rohitronaldo200@gmail.com', to, content)
#     server.close()


#################################### YOUTUBE TOOLS ####################################
# def YoutubeTools():
#         speak("Youtube Tools Started.")
#         notification_message = f"YouTube : YouTube tools are active."
#         notification.notify(
#             title=f"{name_of_ai}",
#             message=notification_message,
#             timeout=3
#         )
#         def done():
#             speak("Done Sir")
#         while comm != "tool exit":
#             speak("Whats Your Command ?")
#             comm = takeCommand()
#             if comm == "":
#                 speak("No command is spoken")
#             elif 'play' in comm:
#                 keyboard.press('space bar')
#                 done()

#             elif 'reset' in comm:
#                 keyboard.press('0')
#                 done()
#             elif 'first' in comm:
#                 pyautogui.moveTo(390,270)

#             elif 'next' in comm:
#                 x,y = pyautogui.position()
#                 print(x)
#                 if x == 390:
#                     pyautogui.moveTo(670,270)
#                 elif x == 670:
#                     pyautogui.moveTo(900,270)
#                 elif x == 900:
#                     pyautogui.moveTo(1200,270)
#                 else:
#                     pyautogui.moveTo(390,270)


#             elif "scroll up" in comm:
#                 pyautogui.scroll(-350)
            
#             elif "page down" in comm:
#                 pyautogui.scroll(3500)


#             elif 'click this' in comm:
#                 pyautogui.click()

#             elif 'new' in comm:
#                 keyboard.press('m')
#                 done()

#             elif 'forward' in comm:
#                 keyboard.press('l')
#                 done()

#             elif 'back' in comm:
#                 keyboard.press('j')
#                 done()

#             elif 'full' in comm:
#                 keyboard.press('f')
#                 done()

#             elif 'film' in comm:
#                 keyboard.press('t')
#                 done()
#             elif 'exit' in comm:
#                 break
#             else:
#                 speak("Command is not in my database.")


#################################### OPEN APPS IN CHROME  ####################################
# def OpenApps():
#         speak("Ok Sir , Wait A Second!")
#         if query == "":
#             speak("Speak it again.")
#         else:
#             if 'chrome' in query:
#                 webbrowser.open('https://google.com/')
            
#             elif 'facebook' in query:
#                 webbrowser.open('https://www.facebook.com/')
            
#             elif 'whatsapp' in query:
#                 webbrowser.open('https://web.whatsapp.com/')

#             elif 'instagram' in query:
#                 webbrowser.open('https://www.instagram.com/')
            
#             elif 'maps' in query:
#                 webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

#             elif 'youtube' in query:
#                 webbrowser.open('https://www.youtube.com')

#             speak("Your Command Has Been Completed Sir!")

#################################### CHROME TOOLS ####################################
# def ChromeTools():
#         speak("Chrome Tools started!")
#         notification_message = f"Chrome : Chrome tools are active."
#         notification.notify(
#             title=f"{name_of_ai}",
#             message=notification_message,
#             timeout=5
#         )
#         while True:
#             command = takeCommand().lower()
#             print("Command is %s" % command)
#             if command == "":
#                 speak("Deactivating Chrome tools")
#             else:
#                 if 'close this tab' in command:
#                     keyboard.press_and_release('ctrl + w')
#                 elif 'open new tab' in command:
#                     keyboard.press_and_release('ctrl + t')
#                 elif 'open new window' in command:
#                     keyboard.press_and_release('ctrl + n')
#                 elif 'history' in command:
#                     keyboard.press_and_release('ctrl +h')
#                 elif 'download' in command:
#                     keyboard.press_and_release('ctrl +j')
#                 elif 'dev' in command:
#                     keyboard.press_and_release('ctrl +shift +i')
#                 elif 'increase size' in command:
#                     keyboard.press_and_release("ctrl + =")
#                 elif 'decrease size'in command:
#                     keyboard.press_and_release("ctrl + -")
#                 elif 'close' in command:
#                     speak("Exitting Chrome.")
#                     keyboard.press_and_release("alt + f4")
#                     break
#                 elif 'exit' in command:
#                     speak("Exitting chrome tools.")
#                     break
#                 else:
#                     speak("Command is not in my database.")


# def WhatsAppTools():
#         speak("What's App Tools started!")
#         notification_message = f"WhatsApp : WhatsApp tools are active."
#         notification.notify(
#             title=f"{name_of_ai}",
#             message=notification_message,
#             timeout=5
#         )
#         while True:
#             command = takeCommand().lower()
#             # command = input('WhatsApp Tools?')
#             if command == "":
#                 speak("Deactivating What's App tools")
#             else:
#                 if 'close whats app' in command:
#                     keyboard.press_and_release('ctrl + w')
#                 elif 'increase size' in command:
#                     keyboard.press_and_release("ctrl + =")
#                 elif 'decrease size'in command:
#                     keyboard.press_and_release("ctrl + -")
#                 elif 'personal info' in command:
#                     pyautogui.click(445,88)
#                 elif 'close info' in command:
#                     pyautogui.click(990, 95)
#                 elif 'send message' in command:
#                     speak("Who you want to send the message?")
#                     sender = takeCommand().lower()
#                     speak(f"What do you want to send {sender}?")
#                     message = takeCommand().lower()
#                     pyautogui.click(305,188)
#                     keyboard.write(f'{sender}')
#                     pyautogui.click(309,243)
#                     sleep(2)
#                     pyautogui.click(786,695)
#                     keyboard.write(f"{message} ")
#                     speak('Do you want to type more then say start!')
#                     break


                    
#                 elif 'start' in command:
#                     speak('What do you want to type.')
#                     while True:
#                         word = takeCommand().lower()
#                         # word = input('Typing?')
#                         if 'stop' in word:
#                             speak('Typing has been stopped.')
#                             break
#                         elif 'none' in word:
#                             pass
#                         elif 'send this message' in word:
#                             speak('Sending your message.')
#                             keyboard.press('enter')
#                         else:
#                             pyautogui.click(786,695)
#                             keyboard.write(f"{word} ")
                        
                        
#                 #################################### EMOJI TOOL ####################################
#                 elif 'emoji tool' in command:
#                     pyautogui.click(443, 693)
#                     while True:
#                         speak("What's your command Sir?")
#                         pyautogui.click(486, 693)
#                         emoji = takeCommand().lower()
#                         # emoji = input("Emoji?")

#                         if 'search' in emoji:
#                             speak("I Am listening.")
#                             search_tool = takeCommand().lower()
#                             # search_tool = input('search tool?')
#                             pyautogui.click(809, 420)
#                             keyboard.write(f"{search_tool} ")
#                         elif 'close emoji' in emoji:
#                             pyautogui.click(443, 693)
#                         elif 'gif' in emoji:
#                             pyautogui.click(527, 693)
#                         elif 'sticker' in emoji:
#                             pyautogui.click(571, 693)
#                         elif 'close' in emoji:
#                             pyautogui.click(443, 693)
#                             break
                        
#                 #################################### ATTACHMENT ####################################
#                 elif 'attachment' in command:
#                     pyautogui.click(485,693)
#                     while True:
#                         speak("What's your command Sir?")
#                         attach = takeCommand().lower()
#                         # attach = input('Attachment?')
#                         if 'photo' in attach:
#                             pyautogui.click(485,635)
#                             break
#                         elif 'camera' in attach:
#                             pyautogui.click(485,567)
#                             break
#                         elif 'document' in attach:
#                             pyautogui.click(485,499)
#                             break
#                         elif 'contact' in attach:
#                             pyautogui.click(485,425)
#                             break
#                         elif 'close' in attach:
#                             break

#                 #################################### SETTINGS ####################################
#                 elif 'open setting' in command:
#                     pyautogui.moveTo(374,132)
#                     sleep(0.2)
#                     pyautogui.click()
#                     sleep(0.2)
#                     pyautogui.click(330,261)
#                     settings = takeCommand().lower()
#                     # settings = input('Setting?')
#                     if 'open profile' in settings:
#                         pyautogui.click(306,273)
                        
                        
#                 #################################### CLOSE WHATSAPP ####################################
#                 elif 'close whatsapp' in command:
#                     speak("Exitting What's App.")
#                     keyboard.press_and_release("ctrl + w")
#                     break
#                 elif 'exit' in command:
#                     speak("Exitting What's App tools.")
#                     break


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
            speak(f"Hello Sir , I Am {name_of_ai} .")
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