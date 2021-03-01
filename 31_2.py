# 5. Запросы к друзьям
# 2. А. Напишите функцию process_friend(name, query), принимающую имя друга name и запрос query.
# Если друга с указанным именем 'Н' нет в списке, то функция должна вернуть сообщение об ошибке У тебя нет друга по имени Н.
# Если запрос — «ты где?», то функция должна вернуть сообщения 'Н в городе Г', где Г определяется по данным словаря DATABASE.
# Если запрос не «ты где?», а какой-то другой, то функция должна вернуть сообщение об ошибке <неизвестный запрос>.
# Б. Допишите функцию process_query(). Если запрос начинается не с «Анфиса», а с другого имени, то вызовите функцию process_friend(name, query), передав в неё имя друга и тело запроса. И верните результат выполнения этой функции.
# В. Добавьте в список queries новые запросы вида:
# Коля, ты где?
# Соня, что делать?
# Антон, ты где?

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'
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
def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?'
    ]
    for query in queries:
        print(query, '-', process_query(query)) 
def process_query(query):
    q=query.split(', ')
    name=q[0]
    if name=='Анфиса':
        return process_anfisa(q[1])
    else: return process_friend(name, q[1])
def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            city = DATABASE[name]
            print(f'{name} в городе {city}')
            return f'{name} в городе {city}'
        else: return '<неизвестный запрос>'
    return f'У тебя нет друга по имени {name}'
runner()

# Результат
# Анфиса, сколько у меня друзей? - У тебя 7 друзей
# Анфиса, кто все мои друзья? - Твои друзья: Сергей, Соня, Миша, Дима, Алина, Егор, Коля
# Анфиса, где все мои друзья? - Твои друзья в городах: Омск, Москва, Пермь, Челябинск, Красноярск
# Анфиса, кто виноват? - <неизвестный запрос>
# Коля в городе Красноярск
# Коля, ты где? - Коля в городе Красноярск
# Соня, что делать? - <неизвестный запрос>
# Антон, ты где? - У тебя нет друга по имени Антон