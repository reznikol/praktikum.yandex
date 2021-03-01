# 3. Передаём параметры в URL
# 1. Запросите погодный сервис http://wttr.in по URL без параметров. А их задайте словарём weather_parameters.
# Функция get() должна принимать его, как отдельный аргумент params.

import requests
url = 'https://wttr.in'
weather_parameters = {
    '0': '',
    'T': ''
}
response = requests.get(url, params=weather_parameters)  # передаем параметры в http-запрос
print(response.text)

print(response.text)

# Результат
# Weather report: Moscow, Russia
# 
#      \  /       Partly cloudy
#    _ /"".-.     +1(-2) °C      
#      \_(   ).   ↗ 31 km/h      
#      /(___(__)  10 km          
#                 0.0 mm         