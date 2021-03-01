# 8. Логические выражения
# 2. Научите Анфису правильно называть количество новых сообщений, когда их меньше 100. Примените логический оператор or и множественное ветвление с elif, чтобы Анфиса выражалась грамотно. К примеру: «У вас 1 новое сообщение», «У вас 35 новых сообщений», «У вас 24 новых сообщения».
# Правильное склонение определяется по последней цифре числительного. Её удобнее всего получать как остаток при делении на 10.
# В коде этого задания он вычисляется оператором модуло %:
# a = 17
# # англ. remainder, «остаток»
# remainder = a % 10  # остаток от деления `a` на 10
# print(remainder)
# # Будет напечатано: 7 
# Анфиса в цикле перебирает все числа от нуля до ста и должна напечатать сто сообщений с правильными склонениями.
# Для каждого числа messages_count Анфиса вычисляет через модуло остаток от деления на десять и сохраняет его в переменную remainder:
# remainder = messages_count % 10 
# Ваша задача — проверить, чему равен remainder и, в зависимости от его значения, задать в коде фразу в правильном склонении.
# Фраза должна оканчиваться словами ...новых сообщений, если:
# остаток от деления на 10 равен нулю,
# остаток от деления на 10 больше либо равен пяти,
# число сообщений — от 11 до 19.
# Например: У вас 20 новых сообщений. У вас 37 новых сообщений. У вас 13 новых сообщений.
# Если остаток от деления на 10 равен единице, текст должен оканчиваться словами ...новое сообщение (внимание: число 11 — исключение из этого правила!).
# Например: У вас 31 новое сообщение.
# В остальных случаях фраза должна оканчиваться словами ...новых сообщения.
# Например: У вас 23 новых сообщения.

for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder ==0 or remainder>=5: 
        print('У вас ' + str(messages_count) + ' новых сообщений')
    elif messages_count >=11 and messages_count <=19:
         print('У вас ' + str(messages_count) + ' новых сообщений')
    elif remainder ==1:
         print('У вас ' + str(messages_count) + ' новое сообщение')
    else:
        print('У вас ' + str(messages_count) + ' новых сообщения')
        
# Результат
# У вас нет новых сообщений
# У вас 1 новое сообщение
# У вас 2 новых сообщения
# У вас 3 новых сообщения
# У вас 4 новых сообщения
# У вас 5 новых сообщений
# У вас 6 новых сообщений
# У вас 7 новых сообщений
# У вас 8 новых сообщений
# У вас 9 новых сообщений
# У вас 10 новых сообщений
# У вас 11 новых сообщений
# У вас 12 новых сообщений
# У вас 13 новых сообщений
# У вас 14 новых сообщений
# У вас 15 новых сообщений
# У вас 16 новых сообщений
# У вас 17 новых сообщений
# У вас 18 новых сообщений
# У вас 19 новых сообщений
# У вас 20 новых сообщений
# У вас 21 новое сообщение
# У вас 22 новых сообщения
# У вас 23 новых сообщения
# У вас 24 новых сообщения
# У вас 25 новых сообщений
# У вас 26 новых сообщений
# У вас 27 новых сообщений
# У вас 28 новых сообщений
# У вас 29 новых сообщений
# У вас 30 новых сообщений
# У вас 31 новое сообщение
# У вас 32 новых сообщения
# У вас 33 новых сообщения
# У вас 34 новых сообщения
# У вас 35 новых сообщений
# У вас 36 новых сообщений
# У вас 37 новых сообщений
# У вас 38 новых сообщений
# У вас 39 новых сообщений
# У вас 40 новых сообщений
# У вас 41 новое сообщение
# У вас 42 новых сообщения
# У вас 43 новых сообщения
# У вас 44 новых сообщения
# У вас 45 новых сообщений
# У вас 46 новых сообщений
# У вас 47 новых сообщений
# У вас 48 новых сообщений
# У вас 49 новых сообщений
# У вас 50 новых сообщений
# У вас 51 новое сообщение
# У вас 52 новых сообщения
# У вас 53 новых сообщения
# У вас 54 новых сообщения
# У вас 55 новых сообщений
# У вас 56 новых сообщений
# У вас 57 новых сообщений
# У вас 58 новых сообщений
# У вас 59 новых сообщений
# У вас 60 новых сообщений
# У вас 61 новое сообщение
# У вас 62 новых сообщения
# У вас 63 новых сообщения
# У вас 64 новых сообщения
# У вас 65 новых сообщений
# У вас 66 новых сообщений
# У вас 67 новых сообщений
# У вас 68 новых сообщений
# У вас 69 новых сообщений
# У вас 70 новых сообщений
# У вас 71 новое сообщение
# У вас 72 новых сообщения
# У вас 73 новых сообщения
# У вас 74 новых сообщения
# У вас 75 новых сообщений
# У вас 76 новых сообщений
# У вас 77 новых сообщений
# У вас 78 новых сообщений
# У вас 79 новых сообщений
# У вас 80 новых сообщений
# У вас 81 новое сообщение
# У вас 82 новых сообщения
# У вас 83 новых сообщения
# У вас 84 новых сообщения
# У вас 85 новых сообщений
# У вас 86 новых сообщений
# У вас 87 новых сообщений
# У вас 88 новых сообщений
# У вас 89 новых сообщений
# У вас 90 новых сообщений
# У вас 91 новое сообщение
# У вас 92 новых сообщения
# У вас 93 новых сообщения
# У вас 94 новых сообщения
# У вас 95 новых сообщений
# У вас 96 новых сообщений
# У вас 97 новых сообщений
# У вас 98 новых сообщений
# У вас 99 новых сообщений