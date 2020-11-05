#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said {}".format(text))

    except:
        print("Sorry We couldn't recognize what you said")
