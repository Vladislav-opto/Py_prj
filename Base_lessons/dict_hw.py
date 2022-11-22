cities = {
    "city": "Москва", 
    "temperature": "20"
}
print(cities["city"])
cities["temperature"] = str(int(cities["temperature"]) - 5)
print(cities)
print(cities.get("country", "Россия"))
cities["date"] = "27.05.2019"
print((len(cities)))