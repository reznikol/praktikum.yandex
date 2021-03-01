# 3. Форматирование строк
# 2. В коде задачи из темы «Циклы и ветвления» замените все объединения строк на f-строки.

def format_text(messages_count):
    remainder = messages_count % 10
    if messages_count == 0:
        return 'нет новых сообщений'
    elif remainder == 0 or remainder >= 5 or (10 <= messages_count <= 19):
        return f'{messages_count} новых сообщений'
    elif remainder == 1:
        return f'{messages_count} новое сообщение'
    else:
        return f'{messages_count} новых сообщения'    
def print_count(messages_count):
    text = format_text(messages_count)
    print(f'У вас {text}.')
print_count(0)
print_count(1)
print_count(4)
print_count(5)
print_count(12)
print_count(22)
print_count(25)

# Результат
# У вас нет новых сообщений.
# У вас 1 новое сообщение.
# У вас 4 новых сообщения.
# У вас 5 новых сообщений.
# У вас 12 новых сообщений.
# У вас 22 новых сообщения.
# У вас 25 новых сообщений.