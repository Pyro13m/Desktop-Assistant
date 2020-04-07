import speech_recognition as sr
from time import ctime
import webbrowser 
import playsound  
import random
from gtts import gTTS
import os,sys

r = sr.Recognizer();

def speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1,100)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            
        voice_data = ''
        audio = r.listen(source)
        
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError: 
            speak("Sorry? You didn't say a word!" )
        except sr.RequestError:
            speak("Service down")
        
        return voice_data


def response(voice_data):
    if 'what is your name' in voice_data:
        speak('Hi! I am Veda. How may I assist you?')
    
    if 'what time is it' in voice_data:
        speak(ctime())
        
    if 'search' in voice_data:
        search = record_audio('What do you want me to search')
        url = 'https://google.co.in/search?q=' + search
        webbrowser.get().open(url)
        speak('Search Results: ' + search)
    if 'video' in voice_data:
        youtube = record_audio('What video you want me to search')
        url = 'https://www.youtube.com/results?search_query=' + youtube
        webbrowser.get().open(url)
        speak('Search Results: ' + youtube)
    if 'translate' in voice_data:
        original = record_audio('What do you want me to translate')
        url = 'https://translate.google.co.in/#view=home&op=translate&sl=auto&tl=hi&text=' + original
        webbrowser.get().open(url)
        speak('Search Results: ' + original)
        
    if 'exit' in voice_data:
        speak('exiting')
        sys.exit()
    
    
speak("How may I assist you?")

print()   
print()

while 1:
    voice_data = record_audio()
    response(voice_data)