from groq import RateLimitError
import socket

from llm.llm_provider import (
    groq_llm,
    groq_llm_with_tools,
    gemini_llm,
    gemini_llm_with_tools
)


def invoke_llm(
    input_data,
    use_tools=False
):

    primary = groq_llm_with_tools if use_tools else groq_llm
    fallback = gemini_llm_with_tools if use_tools else gemini_llm

    try:

        return primary.invoke(input_data)

    except (
        RateLimitError,
        TimeoutError,
        ConnectionError,
        socket.timeout,
        Exception
    ):

        print("Fallback → Gemini")

        return fallback.invoke(input_data)