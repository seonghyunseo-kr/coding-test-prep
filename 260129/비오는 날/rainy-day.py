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
        self.y, self.m, self.d = self.date.split('-')

        
weather_list = []
for i in range(n):
    weather_info = WeatherInfo(date[i], day[i], weather[i])
    weather_list.append(weather_info)

rainy_day = []
for i in range(n):
    if weather_list[i].weather == 'Rain':
        rainy_day.append(weather_list[i])

min_date_y = rainy_day[0].y
min_date_m = rainy_day[0].m
min_date_d = rainy_day[0].d
min_date = rainy_day[0]

for i in range(1, len(rainy_day)):
    if min_date_y > rainy_day[i].y:
        min_date_y = rainy_day[i].y
        min_date = rainy_day[i]

    elif min_date_y == rainy_day[i].y:
        min_date_y = rainy_day[i].y
        if min_date_m > rainy_day[i].m:
            min_date = rainy_day[i]

        elif min_date_m == rainy_day[i].m:
            if min_date_d > rainy_day[i].d:
                min_date = rainy_day[i]
        
print(min_date.date, min_date.day, min_date.weather)
    
