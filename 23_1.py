# 4. Перебор элементов словаря
# 1. Напечатайте о каждом из друзей такое сообщение "<имя друга> живёт в городе <название города>".

friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}
friends['Оля']='Анапа'
friends['Саша']='Краснодар'
print("Вот в каких городах живут мои друзья: "+', '.join(friends.values()))
for friend in friends:
    print(friend+' живет в городе '+friends[friend])
    
# Результат
# Вот в каких городах живут мои друзья: Омск, Москва, Челябинск, Анапа, Краснодар
# Серёга живет в городе Омск
# Соня живет в городе Москва
# Дима живет в городе Челябинск
# Оля живет в городе Анапа
# Саша живет в городе Краснодар