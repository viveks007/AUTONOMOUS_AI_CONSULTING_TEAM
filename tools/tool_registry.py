from tools.calculator_tool import calculator
from tools.datetime_tool import get_current_datetime
from tools.weather_tool import weather_tool
#from tools.web_search_tool import web_search
#from tools.wikipedia_tool import wikipedia
#from tools.sql_tool import sql_tool
#from tools.pdf_reader_tool import pdf_reader


TOOLS = [

    calculator,

    get_current_datetime,

    weather_tool

    #web_search,

    #wikipedia,

    #sql_tool,

    #pdf_reader

]

TOOL_MAP = {

    tool.name: tool

    for tool in TOOLS

}