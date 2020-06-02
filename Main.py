import wikipedia as wiki
import playsound
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import pyttsx3


def welcome():
    print('Welcome to your wiki research assistant.\n'
          'Just say a word of the topic you would like to research.\n')


# function that speaks the input given
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

    return


# function to get audio look it up and speak it
def get_audio():
    # Gets speech recognition audio and recognizes it
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        said = r.recognize_google(audio)
    # Makes sure there is a value
    return said


def wiki_search():
    print("What would you like to research")
    # uses input in wiki summary look up
    user_output = wiki.summary(get_audio())
    # print wiki user_output = wiki summary
    print(user_output)
    # speaks the summary received
    speak(user_output)


def netflix():
    webbrowser.open('http://netflix.com')  # Go to example.com


def funimation():
    webbrowser.open('https://www.funimation.com/')  # Go to example.com


def hulu():
    webbrowser.open('https://www.hulu.com/')  # Go to example.com


i = 0
# runs functions
while i == 0:
    welcome()
    x = get_audio()
    if x == "open Netflix":
        netflix()

    elif x == "open Funimation":
        funimation()

    elif x == "open Hulu":
        hulu()

    elif x == "Wiki search":
        wiki_search()

    elif x == "stop":
        i += 1
