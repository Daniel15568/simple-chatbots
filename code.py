import ollama, os, gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
open_key = os.getenv("OPENAI_API_KEY") 
OPEN_MODEL = "gpt-4-turbo"
