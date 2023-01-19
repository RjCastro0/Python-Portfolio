import pyttsx3
import speech_recognition as sr
import regex as re

#targets a name from voice
def identify_name(text):
    NameError=None
    patterns=["me llamo([A-Za-z])", "mi nombre es([A-Za-z])", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name=re.findall(patterns, text)[0]
        except IndexError:
            print("No me ha dicho su nombre")

    return name

#starts the engine
def initialize_engine():
    engine=pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish") 
    return engine

#hearing function and turns it into text
def recognize_voice(r):
     with sr.Microphone() as source:
        print("Puedes hablar...")
        audio=r.listen(source)
        text=r.recognize_google(audio, lenguage="es-ES")
        return text

#main function
def main():

    initialize_engine()

    engine.say("Hola, como te llamas")
    engine.runAndWait()

    r=sr.Recognizer()
    text=recognize_voice(r)
    name=identify_name(text)

    if name:
        engine.say("Encantado de conocerte,{}".format(name))
        
    else:
        engine.say("no te entiendo mi loco")
        engine.runAndWait()
        

   
        


if __name__=="__main__":
    main()