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

    for repo in data:
        print(f'{repo["name"]} {repo["description"]}')
