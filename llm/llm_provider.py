from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import (
    GROQ_API_KEY,
    GEMINI_API_KEY
)
from tools.tool_registry import TOOLS

from dotenv import load_dotenv
import os

load_dotenv()


groq_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

gemini_llm = ChatGoogleGenerativeAI(
    google_api_key=GEMINI_API_KEY,
    model="gemini-3.5-flash",
    temperature=0.3
)


groq_llm_with_tools = groq_llm.bind_tools(TOOLS)

gemini_llm_with_tools = gemini_llm.bind_tools(TOOLS)