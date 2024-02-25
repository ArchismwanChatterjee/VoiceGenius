import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import google.generativeai as genai
import IPython.display as ipd

genai.configure(api_key="AIzaSyAbVgMWasN83pawqw02-iQHcEJqPQkDl2Y")

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
        st.write("Please speak to ask questions ...")
        audio = recognizer.listen(source, timeout=10)
    try:
        text = recognizer.recognize_google(audio)
        st.write("You said: {}".format(text))
        return text.lower()
    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None


def detect(text):
    prompt_parts = [
        f'''Answer: {text}''', ]
    response = model.generate_content(prompt_parts)
    tts = gTTS(text=response.text, lang='en')
    st.write(response.text)
    tts.save("output.mp3")
    audio_player = ipd.Audio("output.mp3", autoplay=True)
    st.write(audio_player)


def perform_action(command):
    if "what is" in command:
        detect(command)
    else:
        st.warning("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    st.title("Voice-enabled Streamlit App")

    stop_button = st.button("Stop")
    continue_button = st.button("Continue")

    while continue_button:
        if stop_button:
            st.warning("User clicked on Stop. Stopping the continuous listening.")
            break

        user_command = recognize_speech()

        if user_command:
            perform_action(user_command)

        # Sleep to avoid high CPU usage
        # st.experimental_rerun()

    st.write("Continuous listening stopped.")
