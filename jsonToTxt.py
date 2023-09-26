import json

with open('province-city.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('province-city.txt', 'w', encoding='utf-8') as f:
    for province, cities in data.items():
        for city in cities:
            f.write(province + city + '\n')