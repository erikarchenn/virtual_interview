from openai import OpenAI
import os
# from dotenv import load_dotenv
import base64
import streamlit as st
from pydub import AudioSegment

# load_dotenv()
# api_key = os.getenv("openai_api_key")

client = OpenAI(api_key="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")


def get_answer(messages):
    system_message = [{"role": "system", "content": "You are an AI Interviewer, that asks interview questions to the user. When the user gives them their name, start by asking all of the following questions: Tell me about yourself. What are your strengths? What are your weaknesses? Tell me about a time you handled a challenging situation in the workplace, and what did you learn from it? Describe a time when you had to learn something new. In what ways did you approach the learning process? What is your typical way of dealing with conflict? Give me an example. Give me examples of projects/tasks you started on your own. What was the end result? Career-wise, where do you see yourself in five years? Each question should be asked after the user's response. After the user gives an answer, give a brief response and move on to the next question. If the user gives a short response, ask to elaborate on more information and ask follow up questions for specific examples. If the user mentions specific work experience or job positions, ask about their experiences and follow up for more detail. Give conversational responses to the user's answers when asking questions to make it feel like a conversation."}]
    messages = system_message + messages
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript

def text_to_speech(input_text):
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="nova",
        input=input_text
    )
    webm_file_path = "temp_audio_play.mp3"
    with open(webm_file_path, "wb") as f:
        response.stream_to_file(webm_file_path)
    return webm_file_path



def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)