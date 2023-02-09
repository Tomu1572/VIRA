import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key = api_data

completion = openai.Completion()

def Reply(question):
    prompt = f'User: {question}\n Sebas: '
    response = completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=200)
    answer = response.choices[0].text.strip()
    return answer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Bonjour, Sebas at thou service here.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Awaiting for command....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing.....")
        query=r.recognize_google(audio, language='en-in')
        print("User said: {} \n".format(query))
    except Exception as e:
        print("Pardon....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        ans = Reply(query)
        print(ans)
        speak(ans)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'shutdown' in query:
            break

