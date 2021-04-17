import json
#читаем список городов
with open("C:\\Users\\Павел\\IdeaProjects\\weather\\city.list.json", "r", encoding='utf-8') as read_file:
    city_list = json.load(read_file)
#ищем нужный город и его id
for item in city_list:
    if item['name'] == 'Moscow':
        city = 'Moscow'
        id = item['id']
        break
print(city, id)
