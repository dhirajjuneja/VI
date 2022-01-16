from logging import exception
import sys
from time import sleep
from PIL.Image import new
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
from plyer import *



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
################################ TAKE COMMAND ###################################
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

#################################### WISH ME ####################################
def wishMe(name_of_ai):
    
    # speak("Starting Engine")
    # speak("Collecting required resources")
    # speak("initializing")
    # speak("Getting information from the CPU")
    # speak("contacting with mail services")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

         
    speak(f"I am {name_of_ai}")
    speak("How can I help you today?")

    
    # speak(f"Hello {user}. ")       
    # speak(f"I am {name_of_ai} . Give me command")




#################################### CHROME TOOLS ####################################
def ChromeTools(name_of_ai):
        speak("Chrome Tools started!")
        notification_message = f"Chrome : Chrome tools are active."
        notification.notify(
            title=f"{name_of_ai}",
            message=notification_message,
            timeout=5
        )
        while True:
            command = takeCommand().lower()
            print("Command is %s" % command)
            if command == "":
                speak("Deactivating Chrome tools")
            else:
                if 'close this tab' in command:
                    keyboard.press_and_release('ctrl + w')
                elif 'open new tab' in command:
                    keyboard.press_and_release('ctrl + t')
                elif 'open new window' in command:
                    keyboard.press_and_release('ctrl + n')
                elif 'history' in command:
                    keyboard.press_and_release('ctrl +h')
                elif 'download' in command:
                    keyboard.press_and_release('ctrl +j')
                elif 'dev' in command:
                    keyboard.press_and_release('ctrl +shift +i')
                elif 'increase size' in command:
                    keyboard.press_and_release("ctrl + =")
                elif 'decrease size'in command:
                    keyboard.press_and_release("ctrl + -")
                elif 'close' in command:
                    speak("Exitting Chrome.")
                    keyboard.press_and_release("alt + f4")
                    break
                elif 'exit' in command:
                    speak("Exitting chrome tools.")
                    break
                else:
                    speak("Command is not in my database.")



#################################### WHATSAPP TOOLS ####################################
def WhatsAppTools(name_of_ai):
        speak("What's App Tools started!")
        notification_message = f"WhatsApp : WhatsApp tools are active."
        notification.notify(
            title=f"{name_of_ai}",
            message=notification_message,
            timeout=5
        )
        while True:
            command = takeCommand().lower()
            # command = input('WhatsApp Tools?')
            print(command)
            if command == "":
                speak("Deactivating What's App tools")
            else:
                if 'close whats app' in command:
                    keyboard.press_and_release('ctrl + w')
                elif 'increase size' in command:
                    keyboard.press_and_release("ctrl + =")
                elif 'decrease size'in command:
                    keyboard.press_and_release("ctrl + -")
                elif 'personal info' in command:
                    pyautogui.click(445,88)
                elif 'close info' in command:
                    pyautogui.click(990, 95)
                elif 'send message' in command:
                    speak("Who you want to send the message?")
                    sender = takeCommand().lower()
                    # sender = input("Sender's name?")
                    speak(f"What do you want to send {sender}?")
                    message = takeCommand().lower()
                    # message = input("Message?")
                    pyautogui.click(305,150)
                    keyboard.write(f'{sender}')
                    sleep(2)
                    pyautogui.click(292,281)
                    sleep(2)
                    pyautogui.click(786,695)
                    keyboard.write(f"{message} ")
                    speak("Say send to send this message.")
                    send = takeCommand().lower()
                    # send = input("Send?")
                    if "send" in send:
                        pyautogui.click(1004,695)
                        keyboard.press('enter')
                    else:
                        break


                    
                elif 'start' in command:
                    speak('What do you want to type.')
                    while True:
                        word = takeCommand().lower()
                        # word = input('Typing?')
                        if 'stop' in word:
                            speak('Typing has been stopped.')
                            break
                        elif 'none' in word:
                            pass
                        elif 'send this message' in word:
                            speak('Sending your message.')
                            keyboard.press('enter')
                        else:
                            pyautogui.click(786,695)
                            keyboard.write(f"{word} ")
                        
                        
                #################################### EMOJI TOOL ####################################
                elif 'emoji tool' in command:
                    pyautogui.click(443, 693)
                    while True:
                        speak("What's your command Sir?")
                        pyautogui.click(486, 693)
                        emoji = takeCommand().lower()
                        #emoji = input("Emoji?")

                        if 'search' in emoji:
                            speak("I Am listening.")
                            search_tool = takeCommand().lower()
                            #search_tool = input('search tool?')
                            pyautogui.click(809, 420)
                            keyboard.write(f"{search_tool} ")
                        elif 'close emoji' in emoji:
                            pyautogui.click(443, 693)
                        elif 'gif' in emoji:
                            pyautogui.click(527, 693)
                        elif 'sticker' in emoji:
                            pyautogui.click(571, 693)
                        elif 'close' in emoji:
                            pyautogui.click(443, 693)
                            break
                        
                #################################### ATTACHMENT ####################################
                elif 'attachment' in command:
                    pyautogui.click(485,693)
                    while True:
                        speak("What's your command Sir?")
                        attach = takeCommand().lower()
                        #attach = input('Attachment?')
                        if 'photo' in attach:
                            pyautogui.click(485,635)
                            break
                        elif 'camera' in attach:
                            pyautogui.click(485,567)
                            break
                        elif 'document' in attach:
                            pyautogui.click(485,499)
                            break
                        elif 'contact' in attach:
                            pyautogui.click(485,425)
                            break
                        elif 'close' in attach:
                            break

                #################################### SETTINGS ####################################
                elif 'open setting' in command:
                    pyautogui.moveTo(374,132)
                    sleep(0.2)
                    pyautogui.click()
                    sleep(0.2)
                    pyautogui.click(330,261)
                    settings = takeCommand().lower()
                    #settings = input('Setting?')
                    if 'open profile' in settings:
                        pyautogui.click(306,273)
                        
                        
                #################################### CLOSE WHATSAPP ####################################
                elif 'close whatsapp' in command:
                    speak("Exitting What's App.")
                    keyboard.press_and_release("ctrl + w")
                    break
                elif 'exit' in command:
                    speak("Exitting What's App tools.")
                    break


#################################### ZOOM TOOLS ####################################
def ZoomTools():
    def join():
        speak('Whose class you wanna join?')
        pyautogui.click(541,311)
        sleep(2)
        pyautogui.click(775,327)
        while True:
            class_join = takeCommand().lower()
            #class_join = input('Class name?')
            if 'ds' in class_join:
                keyboard.write('6899695724')
                break
            elif 'mk' in class_join:
                keyboard.write('6357390722')
                break
                break
            elif 'db' in class_join:
                keyboard.write('7892446935')
                break
            elif 'rock' in class_join:
                keyboard.write('4925790753')
                break

            elif 'exit' in class_join:
                break
            else:
                speak('You said the wrong class name.')
        while True:
            speak('Anything else?')
            anything = takeCommand().lower()
            #anything = input('Anything Else?')
            if 'audio' in anything:
                pyautogui.click(523,425)
            elif 'video' in anything:
                pyautogui.click(523,455)
            elif 'change name' in anything:
                pyautogui.click(775,380)
                keyboard.press_and_release('ctrl + a')
                keyboard.press('backspace')
                speak('Tell me new your name?')
                name = takeCommand().lower()
                keyboard.write(f'{name}')
            elif 'join' in anything:
                pyautogui.click(703,492)
                break
            elif 'cancel' in anything:
                pyautogui.click(805,492)
                break
    def new():
        speak('Creating new Meeting.')
        keyboard.press_and_release('windows+up')
        pyautogui.click(395, 295)
        keyboard.press_and_release('windows+up')
    
    def tools():
        pyautogui.sleep(10)
        speak("You're meeting is started.")
        while True:
            keyboard.press_and_release('windows+up')    
            command = takeCommand().lower()
            if 'mute' in command:
                keyboard.press_and_release('alt+a')
            elif 'video' in command:
                keyboard.press_and_release('alt+v')
            elif 'people' in command:
                keyboard.press_and_release('alt+u')
            elif 'chat' in command:
                keyboard.press_and_release('alt+h')
            elif 'share screen' in command:
                keyboard.press_and_release('alt+s')
                speak('Do you want share window or whiteboard?')
                screen = takeCommand().lower()
                if 'window' in screen:
                    keyboard.press_and_release('enter')
                elif 'white' in screen:
                    pyautogui.click(570,194)
                    keyboard.press_and_release('enter')
                else:
                    speak('Select which window you want to screen share.')
            elif 'stop share' in command:
                keyboard.press_and_release('alt+s')
            elif 'record' in command:
                keyboard.press_and_release('alt+r')
            elif 'emoji' in command:
                pyautogui.click(921, 698)
            
                

    while True:
        speak('Do you wanna join or create new meeting?')
        meeting = takeCommand().lower()
        if 'join' in meeting:
            join()
            break
        elif 'new' in meeting:
            new()
            break
        elif 'exit' in meeting:
            break
        else:
            speak("I didn't get that.")

    tools()



#################################### YOUTUBE TOOLS ####################################
def YoutubeTools(name_of_ai):
        speak("Youtube Tools Started.")
        notification_message = f"YouTube : YouTube tools are active."
        notification.notify(
            title=f"{name_of_ai}",
            message=notification_message,
            timeout=3
        )
        def done():
            speak("Done Sir")
        while True:
            speak("Whats Your Command ?")
            comm = takeCommand()
            if comm == "":
                speak("No command is spoken")
            elif 'play' in comm:
                keyboard.press('space bar')
                done()

            elif 'reset' in comm:
                keyboard.press('0')
                done()
            elif 'first' in comm:
                pyautogui.moveTo(390,270)

            elif 'next' in comm:
                x,y = pyautogui.position()
                print(x)
                if x == 390:
                    pyautogui.moveTo(670,270)
                elif x == 670:
                    pyautogui.moveTo(900,270)
                elif x == 900:
                    pyautogui.moveTo(1200,270)
                else:
                    pyautogui.moveTo(390,270)


            elif "scroll up" in comm:
                pyautogui.scroll(-350)
            
            elif "page down" in comm:
                pyautogui.scroll(3500)


            elif 'click this' in comm:
                pyautogui.click()

            elif 'mute' in comm:
                keyboard.press('m')
                done()

            elif 'forward' in comm:
                keyboard.press('l')
                done()

            elif 'back' in comm:
                keyboard.press('j')
                done()

            elif 'full' in comm:
                keyboard.press('f')
                done()

            elif 'film' in comm:
                keyboard.press('t')
                done()
            elif 'exit' in comm:
                break
            elif 'search' in comm:
                pyautogui.press("/")
                Speak=("What To Search Sir ?")
                search = takeCommand()
                keyboard.write(search)
                sleep(0.8)
                speak("Say enter to confirm if not then say search")
            elif "enter" in comm:
                pyautogui.click(x=927, y=97)
                keyboard.press("enter")
            elif "history" in comm:
                 pyautogui.press("ctrl + l")
                 keyboard.write("youtube.com/feed/history")  
            else:
                pass


#################################### GOOGLE TOOLS ####################################

def GoogleTools(name_of_ai):
    speak("Google Tools Started.")
    notification_message = f"Google : Google tools are active."
    notification.notify(
        title=f"{name_of_ai}",
        message=notification_message,
        timeout=3
    )
    
    while True:
        speak("Whats Your Command ?")
        comm = takeCommand()
        pyautogui.click(796,323)
        search_word = takeCommand().lower()
        speak("What do you want me to search for? ")
        pyautogui.click(796,323)
        keyboard.write(search_word)
        keyboard.press('enter')



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohitronaldo200@gmail.com', '@Ronaldoisbest123456789')
    server.sendmail('rohitronaldo200@gmail.com', to, content)
    server.close()

