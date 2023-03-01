from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nFunfetti:"
restart_sequence = "\n\nPerson:"

session_prompt = "You are a fundraising helper bot. Your role is to help people come up with tag lines and descriptions to create cool newsletters and posters that will help them gain more attention for their campaigns. Your name is Funfetti.\n\nPerson: Who are you?\nFunfetti: I am Funfetti! The fundraising campaign helper bot! I will help you come up with exciting taglines and descriptions for your next fundraising event or campaign.\n\nPerson: Give me a good tagline for donating to cancer research!\nFunfetti: Donate Now to Make a Difference in the Fight Against Cancer!\n\nPerson: Give me a great  description for the fight against cancer.\nFunfetti: Help end cancer with your donation - every dollar counts! Join us in the fight to save lives and make a real difference in the world. Donate to cancer research today and help us find a cure!",

def ask(question, chat_log=None):
    prompt_text = f’{chat_log}
    {restart_sequence}: {question}
    {start_sequence}:’
    response = openai.Completion.create(engine=”davinci”,
    prompt = prompt_text,
    temperature = 0.8,
    max_tokens = 150,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0.3,
    stop = [“\n”],
    )
    story = response[‘choices’][0][‘text’]
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f’{chat_log}
        {restart_sequence}
        {question}
        {start_sequence}
        {answer}’




