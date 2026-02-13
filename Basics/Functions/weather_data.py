data = [
    {"date": "2025-10-28", "temp": 22, "rain": 5}, #Each dictionary represents the weather for one day.
    {"date": "2025-10-29", "temp": 24, "rain": 0},
]

def get_average_temp(weather):
    total = 0
    for day in weather:    #for day in weather: loops over all the days.
        total += day["temp"]    #day["temp"] accesses the temperature for that day.
    return total / len(weather)

def day_most_rain(weather):
    max_rain = -1   #Sets max_rain to -1 (so any real rain value will be higher).
    day_with_rain = ''
    for day in weather:
        if day["rain"] > max_rain:
            max_rain = day["rain"]
            day_with_rain = day["date"]
    return day_with_rain

print("Average temperature:", get_average_temp(data))
print("Day with most rain:", day_most_rain(data))
