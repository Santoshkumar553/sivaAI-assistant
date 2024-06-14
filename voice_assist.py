import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia



engine= pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
print(voice[0].id)   #This one for testing my system voices
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Hellow Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Hellow Good Afternoon!")

    else:
        speak("Good evening!")

    speak("How can I help you ?")
    

def takecommand():
    '''
    this function help to take the voice command microphone input from the user and returns String as output
    '''

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listning....")
        r.pause_threshold= 0.8
        audio= r.listen(source)

    if query=='Shiva':
        takecommand()

    try:
        print("recogniging......")
        query.adjust_for_ambient_noise(source) 
        query= r.recognize_google_cloud(audio, language='en-US')
        print(f"User said:  {query}\n") 
    except Exception as e:
        # print(e)  Printing the error

        print("See that again please")
        speak("Sorry ! I could not found. Please! Try again")


        return "None"
    
    return query

if __name__== "__main__":
    wishme()

    while True:

        query= takecommand().lower()

        #Executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query= query.replace("wikipedia", "")
            result= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
    