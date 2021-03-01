# 2. Циклы
# 3. Обучим Анфису песенке про непрочитанные письма, сочинённой по мотивам https://ru.wikipedia.org/wiki/99_бутылок_пива.
# Песенка очень простая, куплеты похожи друг на друга. Песня длинная, без сокращений не помещается на экран, но идея ясна и из отрывка: пользователь спрашивает, Анфиса отвечает, число писем уменьшается.
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 10
# Я прочитал одно, и их осталось 9
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 9
# Я прочитал одно, и их осталось 8
# <...>
# Я прочитал одно, и их осталось 2
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 2
# Я прочитал одно, и их осталось 1
# - Анфиса, есть ли новые письма?
# - Одно непрочитанное письмо
# Я прочитал его. И нет больше писем! 
# Напечатайте полный текст этой песенки, организовав цикл так, чтобы код работал с любым исходным значением переменной messages_count.
# Для этого переберите в цикле все числа в диапазоне от messages_count до 1. Перебирать надо от большего значения к меньшему. Код, который выводит последний куплет, должен сработать после окончания цикла.
# Задать список чисел в определённом диапазоне можно так:
# range(первое_число, последнее_число)
# Перевернуть список задом наперёд поможет функция reversed():
# reversed(range(первое_число, последнее_число))

messages_count = 10
for i in reversed(range(2,11)):
    print('- Анфиса, есть ли новые письма?')
    print('- Непрочитанных писем:',i)
    print('Я прочитал одно, и их осталось',i-1)
print('- Анфиса, есть ли новые письма?')
print('- Одно непрочитанное письмо')
print('Я прочитал его. И нет больше писем!')

# Результат
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 10
# Я прочитал одно, и их осталось 9
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 9
# Я прочитал одно, и их осталось 8
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 8
# Я прочитал одно, и их осталось 7
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 7
# Я прочитал одно, и их осталось 6
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 6
# Я прочитал одно, и их осталось 5
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 5
# Я прочитал одно, и их осталось 4
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 4
# Я прочитал одно, и их осталось 3
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 3
# Я прочитал одно, и их осталось 2
# - Анфиса, есть ли новые письма?
# - Непрочитанных писем: 2
# Я прочитал одно, и их осталось 1
# - Анфиса, есть ли новые письма?
# - Одно непрочитанное письмо
# Я прочитал его. И нет больше писем!