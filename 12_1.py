# 6. Множественные ветвления
# 1. Научите Анфису склонять слово «сообщения» в зависимости от их количества:
# для 0 — 'У вас нет новых сообщений'
# для 1 — 'У вас 1 новое сообщение'
# от 2 до 4 — 'У вас # новых сообщения'
# от 5 до 20 — 'У вас # новых сообщений'

for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print('У вас', messages_count, 'новых сообщения')
    else:
        if messages_count > 4:
            print('У вас', messages_count, 'новых сообщений')
            
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