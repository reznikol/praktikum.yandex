# 5. Кириллица в адресной строке
# Вы получили страшный URL. Расшифруйте, какой вопрос задал Яндексу пользователь.
# В ответ напечатайте запрос в чистом виде, без специальных символов.
# Например, он может выглядеть так: что такое помидор.

import urllib.parse
url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'
u=url.split('=')
question =  u[1]
print(urllib.parse.unquote(question))

# Результат
# как бесплатно ездить на такси