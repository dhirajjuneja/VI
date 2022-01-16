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
from backend import speak, takeCommand


#################################### OPEN APPS IN CHROME  ####################################
def OpenApps(query):
        speak("Ok Sir , Wait A Second!")
        if query == "":
            speak("Speak it again.")
        else:
            if 'chrome' in query:
                webbrowser.open('https://google.com/')
            
            elif 'facebook' in query:
                webbrowser.open('https://www.facebook.com/')
                        
            elif 'whatsapp' in query:
                webbrowser.open('https://web.whatsapp.com/')

            elif 'instagram' in query:
                webbrowser.open('https://www.instagram.com/')
            
            elif 'maps' in query:
                webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

            elif 'zoom' in query:
                speak('Opening Zoom.')
                os.system("C:/Users/rohit/AppData/Roaming/Zoom/bin/Zoom.exe")
    
            elif 'youtube' in query:
                webbrowser.open('https://www.youtube.com')

            speak("Your Command Has Been Completed Sir!")
