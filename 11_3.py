# 4. Ветвления
# 3. Как и в прошлой задаче, генерируется случайное значение. Теперь это время на часах.
# Научите Анфису перед знакомством желать вам доброго утра, если в переменной current_hour записано значение меньше 12.

import random  # импорт модуля random
current_hour = random.randint(0, 23) # фукнция randint() генерирует случайное целое число в заданном диапазоне
if  current_hour <12: # напишите условие здесь
    print('Доброе утро!')
    

# Результат
# Доброе утро!