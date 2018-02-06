import speech_recognition as sr
import wikipedia
from gtts import gTTS
from playsound import playsound

speech=sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")

    playsound("audio/ss.mp3")
    audio=speech.listen(source)


try:
    search=speech.recognize_google(audio)
    search_query=gTTS(search,lang="en")			
    search_query.save("audio/search.mp3")

    print("Searching for " + search)
    playsound("audio/sf.mp3")
    playsound("audio/search.mp3")


    summary=wikipedia.summary(search,sentences=1)
    print(summary)
    

    tts=gTTS(summary,lang="en")
    tts.save("audio/wiki.mp3")
    playsound("audio/wiki.mp3")

except:
    print("Run program again")
    playsound("audio/error.mp3")