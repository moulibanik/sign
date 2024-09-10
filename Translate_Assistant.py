import pyttsx3 
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    speak("I am hare to help you out.")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        responses = r.recognize_google(audio, language ='en')
        print(f"user said:{responses}\n")
        
    except Exception as e:
        print("say again please...")
        return "none"
    return responses


if __name__=="__main__":
    speak("hello")
    wishMe()
    
    result = {
        #"QUERY" : "RESULT"
        "hello": "Hello!, how are you baby.",
        "help": "how may i help you.",
        "log in": "start log in.",
        
        # Add more query & result.
    }
    
    while True:   
        responses = takeCommand().lower()
        
        if responses in result:
            result = result[responses] 
            print(result)
            speak(result)
            
        elif 'good' in responses:
            print("Good to see you!")
            speak("good to see you!")
        
        elif 'exit' in responses:
            print("Good Bye!")
            speak("Goodbye!")
            break
        
        else:
            speak("I didn't understand that. Please say this again?")
        
        
