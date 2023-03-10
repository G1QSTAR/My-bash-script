import requests
city = "Moscow,RU"
appid = "47d8548eef32e8c8d677907e9daa2511"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">", "\r\nВетер:",i['wind']['speed'], "\r\nВидимость:",i['visibility'])
    print("____________________________")