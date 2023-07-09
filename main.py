import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime

chatStr = ""


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Tanay: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    # with open(f"OpenAi/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"OpenAi/{''.join(prompt.split('intelligence')[1:1]).strip()}.txt", "w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n **************************** \n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAi"):
        os.mkdir("OpenAi")

    # with open(f"OpenAi/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"OpenAi/{''.join(prompt.split('intelligence')[1:1]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5  # You can change this value although this value is set to 0.8 by default
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")  # For english voice
            # query = r.recognize_google(audio, language="hi-in")  # For hindi voice
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print("Say something")
    say("Hello Sir I am Jarvis. How can i help you?")
    # say("Hello I am. How can i you?")

    while True:
        print("Listening...")
        query = takecommand()

        # todo: Add more sites
        # For opening Websites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "www.Google.com"]]
        for site in sites:
            if f" {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])

        # todo: Add a feature to play more specific songs like you did in websites
        # For opening music
        if "music" in query:
            musicPath = "/Users/tanayrajsrivastava/Downloads/We%20Rollin%20-%20Shubh.mp3"
            os.system(f"open {musicPath}")

        # For Asking time
        elif "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir the time is {strfTime}")

        # todo: Add a feature to open more specific apps like you did in websites
        # For opening any app
        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        # For accessing OpenAI
        elif "Using Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.Lower():
            exit()

        elif "reset chat":
            chatStr = ""

        # For chatting with Jarvis
        else:
            print("Chatting")
            chat(query)

        # todo: Add a feature to find weather in your location
        '''
                API: weatherapi.com
                code
        '''

        # todo: Add a feature to find news in your location
        '''
                API: newsapi.org
                code
        '''

