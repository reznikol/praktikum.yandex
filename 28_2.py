# 2. Метод split()
# 2. Вы умеете звать Анфису. Теперь надо научить её распознавать суть запроса. Отделите обращения — перепишите функцию check_query() так, чтобы она возвращала:
# Например, для запроса 'Анфиса, сколько у меня друзей?' верните строку 'сколько у меня друзей?'.
# Для запроса 'Серёга, ты где?' — строку 'ты где?'.
# У строки, которую она возвращает, не должно быть пробелов в начале и конце.

def check_query(query):
    tokens = query.split(',')
    return tokens[1].strip(' ') 
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]
for q in queries:
    result = check_query(q)
    print(q, '-', result)
    
# Результат
# Анфиса, сколько у меня друзей? - сколько у меня друзей?
# Андрей, ну где ты был? - ну где ты был?
# Андрей, ну обними меня скорей! - ну обними меня скорей!
# Анфиса, кто все мои друзья? - кто все мои друзья?