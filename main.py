from __future__ import print_function
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import subprocess
import ssl
import certifi
from time import ctime
import datetime
import wikipedia
import pyttsx3
import pytz
import pyjokes
import yfinance as yf # to fetch financial data


class person:
    name = ''
    def setName(self, name):
        self.name = name

def contain(texts):
    for text in texts:
        if text in voice_data:
            return True

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source: #Microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError: # error: recognizer does not understand
            print()
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        return voice_data.lower()

def respond(voice_data):
    #User Name   
    if contain(['set name', 'name']):
        person_name = audio('What is you name?')
        name = person_name
        speak(f"okay, i will remember that, {name}")
        person_obj.setName(name) # remember name in person object

    # Time 
    if contain(["what's the time", "tell me the time", "what time is it", 'the time', 'time is it']) :
        time = ctime().split(" ")[3].split(":")[0:2]
        hours = time[0]
        minutes = time[1]
        time = f'{hours}:{minutes}'
        speak(f'{person_obj.name}, It is ' + time)

    #Date
    if contain(["what's the date", "what day is it", 'tell my the date', 'the date', 'day is it', ]) :
        date = ctime()
        day = date[0:3]
        month = date[3:10]
        year = date[19:]
        date = f'{day}{month}{year}'
        speak(f'{person_obj.name}, today is' + date)
    '''
    #Timer
    if contain(["set timer for"]):
    	time = voice_data.split("for")[-1]
    	while t: 
        	mins, secs = divmod(t, 60) 
        	timer = '{:02d}:{:02d}'.format(mins, secs) 
        	print(timer, end="\r") 
        	time.sleep(1) 
        	t -= 1
    '''
    #Play music
    if contain(['play music', 'music']) :
        url = 'https://www.youtube.com/watch?v=_GipmdQMeFQ&list=PLEDnUwQRXV0PbRdcBvEKkSJe7OgPWt0eS&index=26&t=0s'
        webbrowser.get().open(url)

    # Google Search
    if contain(["google"]) :
        search = audio("What would you like to google?")
        url = f'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(f'{person_obj.name}, Here is what I found for ' + search)
    
    #Wikipedia Search
    if contain(['who is', 'what is a', 'what is', 'what are', 'who are']) :
        #thing = audio('What would you like to search for?')
        if 'who is' or 'what is':
            try:
            	term = voice_data.split("is")[-1]
            	wiki = wikipedia.summary(term, sentences=2)
            	speak(f'{person_obj.name}, According to Wikipedia')
            	speak(wiki)
            except:
                search = voice_data.split('is')[-1]
                url = f'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                speak(f'{person_obj.name}, Here is what I found for ' + search)
    
        elif 'what are' or 'who are':
            try:
                term = voice_data.split("are")[-1]
                wiki = wikipedia.summary(term, sentences=2)
                speak(f'{person_obj.name}, According to Wikipedia')
                speak(wiki)
            except: 
                search = voice_data.split('are')[-1]
                url = f'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                speak(f'{person_obj.name}, Here is what I found for ' + search) 
        
        elif 'what is a':
            try:
                term = voice_data.split("a")[-1]
                wiki = wikipedia.summary(term, sentences=2)
                speak(f'{person_obj.name}, According to Wikipedia')
                speak(wiki)
            except:
                search =voice_data.split('a')[-1]
                url = f'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                speak(f'{person_obj.name}, Here is what I found for ' + search)
    
    #Jokes
    if contain(['tell me a joke', 'tell me something funny']):
        speak(pyjokes.get_joke()) 

if __name__ == '__main__': 
    speak("Hello, my name is Enzo. Please set your name")

    WAKE = 'enzo'
    person_obj = person()

    while True:
        print("Listening")
        voice_data = audio()   

        if voice_data.count(WAKE) > 0:
            speak("I am listening")
            voice_data = audio()
            respond(voice_data)
