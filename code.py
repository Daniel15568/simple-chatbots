import ollama, os, gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
open_key = os.getenv("OPENAI_API_KEY") 
OPEN_MODEL = "gpt-4-turbo"

sys_prompt = 'You are an helpful customer service assistant, look through this website https://www.telfordsailingclub.co.uk and answer any questions \
    a customer will have.'
