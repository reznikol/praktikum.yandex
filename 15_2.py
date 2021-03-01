# 2. Функции
# 2. Напишите цикл, в котором функция print_friends_count() вызывается c аргументами от 1 до 10.
# Код самой функции не изменяйте, а цикл пишите после функции, вне её: перед объявлением цикла не должно быть отступов.

def print_friends_count(friends_count):
    remainder = friends_count % 10
    if friends_count == 0:
        print('У тебя нет друзей')
    elif remainder == 0 or remainder >= 5 or (10 <= friends_count <= 19):
        print('У тебя', friends_count, 'друзей')
    elif remainder == 1:
        print('У тебя', friends_count, 'друг')
    else:
        print('У тебя', friends_count, 'друга')
for i in range(1, 11):
    print_friends_count(i)
    
# Результат
# У тебя 1 друг
# У тебя 2 друга
# У тебя 3 друга
# У тебя 4 друга
# У тебя 5 друзей
# У тебя 6 друзей
# У тебя 7 друзей
# У тебя 8 друзей
# У тебя 9 друзей
# У тебя 10 друзей