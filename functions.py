import requests
import configparser
# Данные для работы функций
ids = {'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]}
geo_logs = [{'visit1': ['Москва', '']},
{'visit2': ['Архангельск', '']},
{'visit3': ['Москва', '']},
{'visit4': ['Париж', '']},
{'visit5': ['Лиссабон', '']},
{'visit6': ['Курск', '']},
{'visit7': ['Тула', '']},
{'visit8': ['Владимир', '']},
{'visit9': ['Дели', '']},
{'visit10': ['Барселона', '']}]
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# Задача 1. Функции из домашнего задания коллекция данных
def sorted_list(ids: dict):
    uniq_ids = []
    for val in ids.values():
        uniq_ids += val
    print(sorted(set(uniq_ids)))
    return(sorted(set(uniq_ids)))
def filter_list_function(geo_logs: list):
    filter_list = []
    for element in geo_logs:
        for key, val in element.items():
            if val[1] == 'Россия':
                filter_list.append(element)
    print(filter_list)
    return filter_list
def stats_function(stats: dict):
    a = []
    try:
        for i in stats.values():
            a.append(i)
        max_val = max(a)
        print(list(stats.keys())[list(stats.values()).index(max_val)])
        return(list(stats.keys())[list(stats.values()).index(max_val)])
    except ValueError:
        return ValueError
# Задача 2. Проверка Яндекс API
def get_token():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    token = config["YANDEX_TOKEN"]["token"]
    return token
url = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {'Authorization': get_token()}
params = {'path': 'TEST_FOLDER'}
def create_folder(url, headers, params):
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            requests.put(url, headers=headers, params=params)   
        return response.status_code
