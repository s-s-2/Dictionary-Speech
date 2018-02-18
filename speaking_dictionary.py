import speech_recognition as sr
import time
import json
from difflib import get_close_matches
from gtts import gTTS
import os

data=json.load(open("data.json"))
def func(mytext):
    # The text that you want to convert to audio


    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    sound=mytext.replace(" ","")
    myobj.save(sound+".mp3")

    # Playing the converted file
    os.system(sound+".mp3")
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),cutoff=0.7))>0:
        yn=input("Did you mean '%s' instead? \nEnter Y if Yes, or N if No: " % get_close_matches(w,data.keys())[0])
        if yn == "Y" or yn=="y" or yn==" y" or yn==" Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or yn=="n" or yn==" n" or yn==" N":
            print("Entered word has no meaning!.\nplease double check it.")
        else:
            return "We didn't understand your entry."
    else:
        print("Entered word has no meaning!.\nplease double check it.")
#print("-----Dictionary-----")
#a=int(input("Enter how many words you want to search for :"))
#for i in range(a):
#    word=input("Enter a word: ")
#        for item in output:
#            print('--|>>','"',item,'"')
#    else:
#        print(output)

def speech():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSay something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("\nYou said: " + r.recognize_google(audio))
        return(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
a=int(input("\nHow Many times do you wan to try: "))
while a:
    output=(translate(speech()))
    if type(output) == list:
        for item in output:
            print('The Meaning of your Word is --|>>','"',item,'"')
            func(item)
    else:
        print(output)
    a=a-1



time.sleep(5)
