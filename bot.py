from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import subprocess

def talk(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('say '+audio)
    

def makeItHappen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk("Give me something to do")
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(command)

    except sr.UnknownValueError:
        assistant(makeItHappen()) 

    return command



def assistant(command):
    if 'coding dojo' in command:
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = 'https://learn.codingdojo.com/dashboard'
        webbrowser.get(chrome_path).open(url)

    if 'what is the weather' in command:
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = 'https://www.google.com/search?q=weather'
        webbrowser.get(chrome_path).open(url)

    if 'where am I' in command:
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = 'https://www.google.com/search?q=my%20location'
        webbrowser.get(chrome_path).open(url)

    if 'how is the stock market' in command:
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = 'https://money.cnn.com/data/markets/'
        webbrowser.get(chrome_path).open(url)

    if 'open music' in command:
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = 'https://www.spotify.com/us/'
        webbrowser.get(chrome_path).open(url)

    if 'hello' in command:
        talk('Whats up brother man')

    if 'how are you' in command:
        talk('I am stuck in your computer')

    if 'say something funny' in command:
        talk('Your mom')



while True:
    assistant(makeItHappen())