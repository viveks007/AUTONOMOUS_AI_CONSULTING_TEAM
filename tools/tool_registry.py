from tools.calculator_tool import calculator
from tools.datetime_tool import get_current_datetime
from tools.weather_tool import weather_tool
from tools.google_drive_tool import google_drive_tool



TOOLS = [

    calculator,

    get_current_datetime,

    weather_tool,

    google_drive_tool

    #web_search,

    #wikipedia,

    #sql_tool,

    #pdf_reader

]

TOOL_MAP = {

    tool.name: tool

    for tool in TOOLS

}