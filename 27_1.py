# 9. Прототип запроса к базе данных
# 1. Допишите в runner() вызов функции process_query() с аргументом 'Где все мои друзья?'.
# Запустите, и удостоверьтесь, что Анфиса видит запрос. Пусть она и не понимает, что предпринять в ответ.

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
def format_friends(friends_count):
    if friends_count == 1:
        return 'У тебя 1 друг'
    elif 2 <= friends_count <= 4:
        return 'У тебя ' + str(friends_count) + ' друга'
    elif friends_count >= 5:
        return 'У тебя ' + str(friends_count) + ' друзей'
def process_query(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return format_friends(count)
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return 'Твои друзья: ' + friends_string
    else:
        return '<неизвестный запрос>'
def runner():
    print('Привет, я Анфиса!')
    print(process_query('Сколько у меня друзей?'))
    print(process_query('Кто все мои друзья?'))
    print(process_query('Где все мои друзья?'))
runner()

# Результат
# Привет, я Анфиса!
# У тебя 7 друзей
# Твои друзья: Серёга, Соня, Миша, Дима, Алина, Егор, Коля
# <неизвестный запрос>