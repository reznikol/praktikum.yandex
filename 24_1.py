# 5. Множества
# 1. Сделайте из списка cities сет unique_cities, где записаны по разу названия городов, в которых живут ваши друзья. После этого напечатайте строку из элементов unique_cities на экран через запятую и пробел — да, join() работает и для множеств тоже!

cities = ['Вологда', 'Чебоксары', 'Тольятти', 'Вологда']
unique_cities =set(cities) 
print(', '.join(unique_cities))

# Результат
# Тольятти, Вологда, Чебоксары