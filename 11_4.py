# 4. Ветвления
# 4. это время на часах.
# Научите Анфису перед знакомством желать вам доброго утра, если в переменной current_hour записано значение меньше 12.
# Расширьте код из прошлой задачи. Если на часах полдень или позже — пусть Анфиса скажет: 'Добрый день!'
import random  # импорт модуля random
current_hour = random.randint(0, 23) # фукнция randint() генерирует случайное целое число в заданном диапазоне
if  current_hour <12: # напишите условие здесь
    print('Доброе утро!')
else:
    print('Добрый день!')
    
# Результат
# Доброе утро!