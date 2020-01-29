# 1. Посмотреть документацию к API GitHub,
# разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json

user = input('Введите имя пользователя: ')
url = f'https://api.github.com/users/{user}/repos'

response = requests.get(url)

if (response.ok):
    data = json.loads(response.text)
    print(f'\nСписок репозиториев пользователя {user}\n')

    if not data:
        print('Репозиториев не найдено')
    else:
        for repo in data:
            print(f'{repo["name"]} {repo["description"]}')

        with open('repos.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)


