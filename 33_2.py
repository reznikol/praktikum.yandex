# 3. Работа со временем
#2. Напишите код, отвечающий на запрос пользователя Сколько времени у меня уже ушло на вводный курс по бэкенд-разработке?
# Вспомните, в какой день и во сколько вы начали проходить курс.
# Запишите этот момент времени в переменную start_moment. В переменную current_moment запишите текущий момент времени.
# Затем вычислите разницу двух этих моментов, запишите её в переменную total_time, и напечатайте её на экране.

import datetime as dt
start_moment = dt.datetime(2020, 11, 14, 10, 13, 0)  # напишите код здесь
current_moment = dt.datetime(2021, 1, 3, 9, 26, 0)  # напишите код здесь
total_time = current_moment-start_moment  # и здесь
print(total_time)

# Результат
# 49 days, 23:13:00