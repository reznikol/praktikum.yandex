# 9. Вызов функции из функции
# Измените код Анфисы. Оставьте вывод на экран, т.е. вызовы функции print(), только в одном месте — в основном теле программы. Эти вызовы уже написаны в предварительном коде задания.
# Все прошлые выводы на экран — в функциях show_count_friends() и process_query() — замените на возвращения результатов из функции оператором return.

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
def show_count_friends(count_friends):
    if count_friends == 1:
        text='У тебя 1 друг'
    elif 2 <= count_friends <= 4:
        text='У тебя ' + str(count_friends) + ' друга'
    elif count_friends >= 5:
        text='У тебя ' + str(count_friends) + ' друзей'
    return text

def process_query(query):
    if query == 'Сколько у меня друзей?':
        count = len(FRIENDS)
        return show_count_friends(count)
       
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(FRIENDS)
        text='Твои друзья: ' + friends_string
    else:
        text='<неизвестный запрос>'
    return text

def runner():
    print(process_query('Сколько у меня друзей?'))
    print(process_query('Кто все мои друзья?'))
    print(process_query('Как меня зовут?'))
runner()

# Результат
# У тебя 5 друзей
# Твои друзья: Серёга, Соня, Дима, Алина, Егор
# <неизвестный запрос>