import streamlit as st

import speech_recognition as sr
from gtts import gTTS
import google.generativeai as genai

import IPython.display as ipd
import time

from mutagen.mp3 import MP3
import os
# from pydub import AudioSegment


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("MY_SECRET_KEY")) 

# Set up the model

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        with st.chat_message("assistant"):
            if c == 0:
                st.write("Please speak to ask questions ...")
            else:
                st.write("Please speak to ask the next question or click on STOP ...")
        audio = recognizer.listen(source, timeout=10)
    try:
        text = recognizer.recognize_google(audio)
        with st.chat_message("user"):
            st.write("User: {}".format(text))
        return text.lower()
    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def detect(text):
    prompt_parts = [f'''Answer: {text}''', ]
    response = model.generate_content(prompt_parts)

    tts = gTTS(text=response.text, lang='en')
    tts.save("output.mp3")

    audio = MP3("output.mp3")
    audio_duration = audio.info.length

    with st.chat_message("assistant"):
        st.write("Bot: {}".format(response.text))
        audio_player = ipd.Audio("output.mp3", autoplay=True)
        st.write(audio_player)
        time.sleep(audio_duration)

        return response.text, audio_duration

def perform_action(command):
    if any(word in command for word in ["what", "how", "why", "where", "when", "who", "which"]):
        answer, duration = detect(command)
        return answer, duration
    else:
        st.warning("Sorry, I didn't understand that command.")
        return None, 0

if __name__ == "__main__":

    st.image("logo.png", width=200)

    st.title("VoiceGenius : A new way to interact with AI")
    
    st.info("Start the question by saying What/Why/Where/When/Who/Which/How <your question>.")

    disclaimer_message = """This is a voice based GPT, where the user will be able to communicate with the GPT through voice. Kindly follow the instructions for best results 🙂. Currently it has a rate limit of 5 chats. The users will be able to download the conversation after the app STOP's """

    st.write("")
    with st.expander("Disclaimer ⚠️", expanded=False):
        st.markdown(disclaimer_message)

    stop_button = st.button("STOP")
    continue_button = st.button("START")

    c = 0

    conversation = []  

    while continue_button:
        if stop_button:
            st.warning("User clicked on Stop.")
            break

        user_command = recognize_speech()

        c += 1

        if user_command:
            answer, audio_duration = perform_action(user_command)
            if answer:
                conversation.append(f"User: {user_command}\nBot: {answer}\n")

    # Store conversation in a file after each question and answer
        with open("output.txt", "a") as file:
            for entry in conversation:
                file.write(entry)
                file.write("\n")
        
        conversation = []  
        time.sleep(2)

        if c == 5:
            break

    if c == 5:
        st.write("Limit of 5 chats at a stretch is reached. Restart the app to continue.")
        
        if st.button('Rerun App'):
            st.experimental_rerun()
    else:
        st.write("Click on START to start, and if you want to stop anytime, then click on STOP.")

    # Store conversation in a file
    with open("output.txt", "a") as file:
        for entry in conversation:
            file.write(entry)


    with open("output.txt", "r") as file:
        conversation = file.read()
    
    
    st.download_button(
        label="Download Conversation",
        data=conversation,
        file_name="conversation.txt",
        key="download_button"
    )



