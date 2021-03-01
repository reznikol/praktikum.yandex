# 3. Аргументы функции
# По задумке программиста функция print_friends_count() должна принять на вход два аргумента: имя человека и число (количество его друзей), а в результате работы вывести радостную фразу '{имя}, у тебя {количество} друзей'
# Например: Лера, у тебя 18 друзей.
# Или: Коля, у тебя 1 друг.
# А если имя неизвестно — тогда фраза должна быть такая: 'У тебя {количество} друзей'. Например: У тебя 10 друзей.
# В начале функции в переменную text сохраняется слово «друг» в нужном склонении, в зависимости от значения переменной friends_count. Этот фрагмент кода работает, изменять его не нужно.
# Но функцию нужно дописать: сейчас она принимает лишь один аргумент (количество друзей) и ничего не печатает.
# Допишите функцию print_friends_count() так, чтобы она принимала второй аргумент: name (в него будет передаваться имя)
# На случай, если аргумент name не будет передан — установите для него значение по умолчанию: пустую строку.
# В функцию добавьте проверку:
# Если в переменной name содержится имя (если в ней не пустая строка) — функция должна напечатать '{имя}, у тебя {количество} друзей'
# Если же в переменной name содержится пустая строка — должно быть напечатано 'У тебя {количество} друзей'

def print_friends_count(friends_count, name=''):
    if friends_count == 1:
        text = '1 друг'
    elif 2 <= friends_count <= 4:
        text = str(friends_count) + ' друга'
    elif friends_count >= 5:
        text = str(friends_count) + ' друзей'
    if name != '':
        print (name + ', у тебя ' + text)
    else:
        print ('У тебя ' + text)
print_friends_count(3, 'Артём')
print_friends_count(friends_count=7, name='Марина')
print_friends_count(6)
print_friends_count(4, name='Настя')

# Результат
# Артём, у тебя 3 друга
# Марина, у тебя 7 друзей
# У тебя 6 друзей
# Настя, у тебя 4 друга