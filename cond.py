#Weather Reporter : Take city and print fake/random weather info.
import random

def get_fake_weather(city):
    temperatures = list(range(-10, 41))  # -10°C to 40°C
    conditions = ["Sunny", "Rainy", "Cloudy", "Snowy", "Windy", "Thunderstorms", "Foggy", "Humid"]
    humidity = random.randint(20, 100)   # percent
    wind_speed = round(random.uniform(1, 20), 1)  # km/h

    weather_info = {
        "Temperature": f"{random.choice(temperatures)}°C",
        "Condition": random.choice(conditions),
        "Humidity": f"{humidity}%",
        "Wind Speed": f"{wind_speed} km/h"
    }

    print(f"\n📍 Weather Report for {city.title()}:")
    for key, value in weather_info.items():
        print(f"→ {key}: {value}")

city_name = input("Enter a city name: ")
get_fake_weather(city_name)


