# 2. Что такое библиотеки?
# Научите Анфису отвечать на вопрос «Анфиса, как дела?» случайным образом.
# Для этого напишите функцию how_are_you() без параметров (да-да, функции могут не иметь параметров, это нормально).
# Пусть она возвращает случайный ответ из списка answers. Можете и сами дописать варианты :)

from random import choice as k 
answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду', 'Гуд', 'Потихоньку']
def how_are_you():
    return k(answers)
print(how_are_you())

# Результат
# Отличненько!