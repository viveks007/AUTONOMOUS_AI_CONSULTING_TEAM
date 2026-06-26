from langchain_core.tools import tool

from datetime import datetime


@tool
def get_current_datetime() -> str:
    """
    Returns the current date, time,
    weekday, month, year and quarter.
    """

    now = datetime.now()

    quarter = (now.month - 1) // 3 + 1

    return f"""
Current Date : {now.strftime("%d-%m-%Y")}

Current Time : {now.strftime("%H:%M:%S")}

Weekday : {now.strftime("%A")}

Month : {now.strftime("%B")}

Year : {now.year}

Quarter : Q{quarter}
"""