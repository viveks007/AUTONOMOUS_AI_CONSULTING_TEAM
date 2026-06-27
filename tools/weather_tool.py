from langchain_core.tools import tool

from mcp_servers.weather_client import get_weather


@tool
def weather_tool(city: str) -> str:
    """
    Get current weather for a city.
    """

    weather = get_weather(city)

    return f"""
        City: {weather['city']}

        Country: {weather['country']}

        Temperature: {weather['temperature']} °C

        Condition: {weather['condition']}

        Humidity: {weather['humidity']} %

        Wind Speed: {weather['wind_kph']} km/h
        """