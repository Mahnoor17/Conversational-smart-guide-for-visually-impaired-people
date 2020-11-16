#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
def recognizeSpeech():
    text="Google Speech Recognition could not understand audio"
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Say something!")
        audio = r.listen(source,phrase_time_limit=5)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text="You said: " + r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text