#copilot
import requests

def get_weather_by_address(city_name):
    api_key = "132f97be3cc87c20986a74d0b41dc0b2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        weather_info = (f"Temperature: {temperature}°C\n"
                        f"Atmospheric Pressure: {pressure} hPa\n"
                        f"Humidity: {humidity}%\n"
                        f"Description: {description}")
        return weather_info
    else:
        return "City not found."


