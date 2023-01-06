import requests, settings

def weather_by_city(city_name: str) -> dict|None:
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": settings.API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru",
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except(IndexError, TypeError):
                    return None
    except(requests.RequestException, ValueError):
        return None
    return None

if __name__ == "__main__":
    print(weather_by_city("Moscow,Russia")) 