# 5. Обработка ошибок
# 2. Это задание — финальное. В нём вы сделаете Анфису мастером на все руки. Анфиса будет знать всё про ваших друзей — где они, сколько у них времени, и какая у них погода.
# В список запросов queries в функции runner() добавлены новые запросы про погоду:
# Коля, как погода?
# Соня, как погода?
# Антон, как погода?
# Научите Анфису отвечать на вопросы такого вида. Для этого:
# Добавьте в функцию process_friend() обработку ещё одного запроса 'как погода?'. Для получения ответа на этот вопрос используйте значение city — это город, в котором живёт друг.
# Затем вызовите функцию what_weather() — вы написали на прошлом уроке почти такую же. Она уже доступна в коде этого задания.
# Верните результат выполнения этой функции как результат process_friend().

import datetime as dt
import requests
DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}
UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}
def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'
def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time
def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды>'
def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'
def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<не могу определить время в городе {city}>'
            time = what_time(city)
            return f'Там сейчас {time}'
        elif query == 'как погода?':
            if city in DATABASE[name]:
                return what_weather(city)     
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'
def process_query(query):
    tokens = query.split(', ')
    name = tokens[0]
    if name == 'Анфиса':
        return process_anfisa(tokens[1])
    else:
        return process_friend(name, tokens[1])
def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?',
        'Коля, как погода?',
        'Соня, как погода?',
        'Антон, как погода?'
    ]
    for query in queries:
        print(query, '-', process_query(query))
runner()

# Результат
# Анфиса, сколько у меня друзей? - У тебя 10 друзей
# Анфиса, кто все мои друзья? - Твои друзья: Сергей, Соня, Алексей, Миша, Дима, Алина, Егор, Коля, Артём, Петя
# Анфиса, где все мои друзья? - Твои друзья в городах: Челябинск, Омск, Пермь, Красноярск, Калининград, Москва, Михайловка, Владивосток
# Анфиса, кто виноват? - <неизвестный запрос>
# Коля, ты где? - Коля в городе Красноярск
# Соня, что делать? - <неизвестный запрос>
# Антон, ты где? - У тебя нет друга по имени Антон
# Алексей, который час? - Там сейчас 13:46
# Артём, который час? - Там сейчас 21:46
# Антон, который час? - У тебя нет друга по имени Антон
# Петя, который час? - <не могу определить время в городе Михайловка>
# Коля, как погода? - 🌨  🌡️-18°C 🌬️↖1.1m/s
# Соня, как погода? - ⛅️  🌡️+1°C 🌬️↗5.3m/s
# Антон, как погода? - У тебя нет друга по имени Антон