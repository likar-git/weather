import json
import requests
appid = 'd19b2b422c0755e561aaa39961633ca0'
#читаем список городов
with open("C:\\Users\\Павел\\IdeaProjects\\weather\\city.list.json", "r", encoding='utf-8') as read_file:
    city_list = json.load(read_file)
#ищем нужный город и его id
city = input()
for item in city_list:
    if item['name'] == city:
        city = item['name']
        id = item['id']
        break
print(city, id)
