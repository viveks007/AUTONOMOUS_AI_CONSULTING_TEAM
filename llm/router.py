from groq import RateLimitError

from llm.llm_provider import (
    groq_llm_with_tools,
    gemini_llm_with_tools
)

import socket


def invoke_llm(prompt):

    try:

        return groq_llm_with_tools.invoke(prompt)

    except (
        RateLimitError,
        TimeoutError,
        ConnectionError,
        socket.timeout,
        Exception
    ):

        print("Fallback → Gemini")

        return gemini_llm_with_tools.invoke(prompt)