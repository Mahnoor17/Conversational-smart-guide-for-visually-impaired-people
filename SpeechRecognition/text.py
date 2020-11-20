'''import pyttsx3
engine = pyttsx3.init()
engine.say("Hi I am Mahnoor Salahuddin, a student of bachelors in computer science")
engine.runAndWait()
engine.stop()'''

# Import the gTTS module for text  
# to speech conversion  
from gtts import gTTS  
from datetime import datetime
import os
  
# This module is imported so that we can  
# play the converted audio  
  
from playsound import playsound  
def text(text_val):
    # It is a text value that we want to convert to audio  
    #text_val = input("Enter your text: ")  
      
    # Here are converting in English Language  
    language = 'en'  
      
    # Passing the text and language to the engine,  
    # here we have assign slow=False. Which denotes  
    # the module that the transformed audio should  
    # have a high speed  
    obj = gTTS(text=text_val, lang=language, slow=False)  
      
    #Here we are saving the transformed audio in a mp3 file named  
    # exam.mp3  
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    obj.save(filename)    
    # Play the exam.mp3 file  
    playsound(filename)   
    return text
#text("Hi I am Mahnoor Salahuddin, a student of bachelors in computer science")
