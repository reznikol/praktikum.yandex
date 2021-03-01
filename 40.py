# 4. Заголовки запросов и ответов
# На прошлом уроке вы заказывали страницу на русском языке через параметры в URL.
# Сейчас сделайте то же самое, только русский язык запрашивайте через заголовок запроса 'Accept-Language'.

import requests
url = 'https://wttr.in'
weather_parameters = {
    '0': '',
    'T': '',
    'M': ''
}
request_headers = {
    'Accept-Language': 'ru'
}
response=requests.get(url, params=weather_parameters, headers=request_headers) # передаем параметры и заголовки в http-запрос через аргументы `params` и `headers` функции get()
print(response.text)

# Результат
# Прогноз погоды: Moscow, Russia
# 
#      \  /       Переменная облачность
#    _ /"".-.     +1(-2) °C      
#      \_(   ).   ↗ 5 m/s        
#      /(___(__)  10 km          
#                 0.0 mm         