n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class WeatherInfo:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
        
weather_list = []
for i in range(n):
    weather_info = WeatherInfo(date[i], day[i], weather[i])
    weather_list.append(weather_info)

rainy_day = []
for i in range(n):
    if weather_list[i].weather == 'Rain':
        rainy_day.append(weather_list[i])

min_date_obj = rainy_day[0]

for i in range(1, len(rainy_day)):
    if rainy_day[i].date < min_date_obj.date:
        min_date_obj = rainy_day[i]

print(f"{min_date_obj.date} {min_date_obj.day} {min_date_obj.weather}")