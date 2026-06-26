from groq import RateLimitError
import socket

from llm.llm_provider import (
    groq_llm_with_tools,
    gemini_llm_with_tools
)


def invoke_llm(input_data):

    try:

        return groq_llm_with_tools.invoke(input_data)

    except (
        RateLimitError,
        TimeoutError,
        ConnectionError,
        socket.timeout,
        Exception
    ):

        print("Fallback → Gemini")

        return gemini_llm_with_tools.invoke(input_data)