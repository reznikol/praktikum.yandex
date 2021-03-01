# 5. Разбиение на функции
# 1.
# Подготовьте код Анфисы к использованию на сервере.
# Напишите функцию process_query(). Перенесите в неё весь код из тела основной программы. Эта функция будет принимать на вход запросы пользователя и выдавать ответ на них. Пока она может обработать всего один запрос — сообщить количество друзей.
# Добавьте вызов функции process_query() в тело основной программы.

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')
def process_query():
    print("Привет, я Анфиса!")
    count = len(FRIENDS)
    print_friends_count(count)
process_query()

# Результат
# Привет, я Анфиса!
# У тебя 5 друзей