import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")