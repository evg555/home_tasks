# 2. Изучить список открытых API. Найти среди них любое,
# требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию.
# Ответ сервера записать в файл

# Будет использованно API Вконтакте и выведен и сохранен список друзей пользователя

import requests
import json

# Нужно ввести полученный access_token в приложении в ВК (свой в рамках безопасности не указываю)
token = ''

order = 'hints'
count = 100
fields = 'first_name,last_name'
v = '5.103'
url = f'https://api.vk.com/method/friends.get?order={order}&count={count}&fields={fields}&v={v}&access_token={token}'

response = requests.get(url)

if (response.ok):
    data = json.loads(response.text)

    print(f'Список друзей текущего пользователя\n')

    if data['error']:
        print('Ошибка получения данных')
    else:
        for friend in data['response']['items']:
            print(f'{friend["first_name"]} {friend["last_name"]}')

        with open('friends.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
