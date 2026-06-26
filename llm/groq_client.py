from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY
from tools.tool_registry import TOOLS

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


llm_with_tools = llm.bind_tools(
    TOOLS
)