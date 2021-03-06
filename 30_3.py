# 4. Подробнее о форматировании
# 3. Анфисе передали список listened (англ. listen, «слушать») с хронометражем прослушанных песен в секундах. Выведите на экран суммарную статистику:
# 'Вы прослушали N песен, общей продолжительностью M минут и S секунд.'
# Где:
# N — длина списка listened;
# M — количество целых минут общей продолжительности прослушанного;
# S — остаток от целых минут.

def calc_stat(listened):
    N=len(listened)
    M=sum(listened)//60
    S=sum(listened)%60
    return f'Вы прослушали {N} песен, общей продолжительностью {M} минут и {S} секунд.'
print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))

# Результат
# Вы прослушали 10 песен, общей продолжительностью 30 минут и 14 секунд.