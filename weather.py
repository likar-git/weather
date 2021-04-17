import json
import requests
appid = 'd19b2b422c0755e561aaa39961633ca0'
#читаем список городов
with open("C:\\Users\\Павел\\IdeaProjects\\weather\\city.list.json", "r", encoding='utf-8') as read_file:
    city_list = json.load(read_file)
#ищем нужный город и его id
# city = input()
city = 'Moscow'
for item in city_list:
    if item['name'] == city:
        city = item['name']
        city_id = item['id']
        break
print(city, id)
current = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

data = current.json()
print('Погода:', data['weather'][0]['description'])
print('Температура:', data['main']['temp'])
print('Минимальная температура:', data['main']['temp_min'])
print('Максимальная температура:', data['main']['temp_max'])