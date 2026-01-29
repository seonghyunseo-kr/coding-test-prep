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
    def date_split(self):
        y, m, d = self.date.split('-')
        return int(y), int(m), int(d)
        
weather_list = []
for i in range(n):
    weather_info = WeatherInfo(date[i], day[i], weather[i])
    y, m, d = weather_info.date_split()
    weather_list.append(weather_info, y, m, d)

min_date_y = weather_list[0]
for i in range(n):
    print(weather_list[i])