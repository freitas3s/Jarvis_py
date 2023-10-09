import speech_recognition as sr
import os 
from gtts import gTTS
import datetime
import calendar
import warnings
import random
import wikipedia

warnings.filterwarnings('ignore')

def recordAudioAsString():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio= r.listen(source)
    data= ''

    try:
        data = r.recognize_google(audio)
        print("you said:" +data)
    except sr.UnknownValueError:
        print("We can not understend the audio,unknown error")
    except sr.RequestError as e:
        print('service error'+e)

    return data

def getJarvisResponse(inputCommandText):
    print(inputCommandText)
    obj = gTTS(text=inputCommandText, lang="en", slow=False)
    obj.save('jarvis_response.mp3')
    os.system("afplay jarvis_response.mp3")

def iceBreakingWords(text):
    words = ["Hey Freitas, how may I help you?","okay freitas", "jarvis welcomes you"]
    
    for w in words:
        if text in text:
            return True

def getDate():
    now = datetime.now()
    current_date = datetime.datetime.today()
    current_day = calendar.day_name[current_date.weekday()]
    month = now.month
    day = now.day
    month_list = ["Janeiro","Fevereiro", "Março", "Abril","Maio","junho","Julho","Agosto","setembro","Outubro","Novembro","Dezembro"]
    ordinal = lambda n: "%d%s" %(n,"tsnrhtdd"[(n//10 % 10 != 1)*(n%10<4) * n % 10::4])
    ordinal_list = [ordinal(n)for n in range(1,32)]

    return "Today is" + current_day + ' '+ month_list [month-1] + ' ' +ordinal_list[day-1]

def greet (text):
    input_greet_words = ["hi","hello"]
    output_greet_words = ["hello,how cani help you?","hey,wassup"]

    for word in text.split():
        if word in input_greet_words:
            return random.choice(output_greet_words)

    return '  '

def getPersonData (text):
    text_list = text.split()
    for i in range(0,len(text_list)):
        if i<=len(text_list) and text_list[i].lower()== "who" and text_list[i+1].lower()=="is":
            #print(text_list[2] + ' ' + text_list[3])
            return text_list[2] + ' ' + text_list[3]
        


while True:
    text = recordAudioAsString()
    response = ''

    if greet(text):
        response = response + greet(text)

        if "date" in text:
            get_date = getDate()
            response = response + ' ' + get_date
        
        if "who is" in text:
            person = getPersonData(text)
            wiki = wikipedia.summary(person,senteces = 2)
            response = response + " " + wiki

    getJarvisResponse(response)
