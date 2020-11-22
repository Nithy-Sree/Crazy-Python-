#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

# this class is to recognize speech
r = sr.Recognizer()

# instead of using an audio file as the source, use the default system microphone
# by creating the instance of Microphone Class
with sr.Microphone() as source:
    print("Speak Anything")
    # this method is for reducing the noise occured while recording the speech
    r.adjust_for_ambient_noise(source)
    
    # this is used to listen to the audio(speech)
    audio = r.listen(source)

    try:
        # using google web speech api we are converting to text
        # we do have several methods microsoft bing speech, google cloud api and so on
        text = r.recognize_google(audio)
        print("You said {}".format(text))

    except:
        # if the audio is not recorded properly print not clear
        print("Sorry We couldn't recognize what you said")
