import ollama, os, gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
open_key = os.getenv("OPENAI_API_KEY") 
OPEN_MODEL = "gpt-4-turbo"

sys_prompt = 'You are an helpful customer service assistant, look through this website https://gresford-sailing-club-gsc.github.io/index/ \
and answer any questions a customer will have.'

def chat(message, history):
    messages = [{'role':'system', 'content':system}]
    for user_message, assistant_message in history:
        messages.append({'role':'user', 'content':user_message})
        messages.append({'role':'assistant', 'content':assistant_message})
    messages.append({'role':'user', 'content':message})
    
    print('History is: ')
    print(history)
    print('Message is: ')
    print(message)

    output = openai.chat.completions.create(model=OPEN_MODEL, messages=messages, stream=True)
    stream = ''
    for chunk in output:
        stream += chunk.choices[0].delta.content or ''
        yield stream
