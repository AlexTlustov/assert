import pytest
from functions import *

@pytest.mark.parametrize("data_input, expected_output", [
    ({}, []),
    ({'user1': []}, []),
    ({'user1': [2, 3, 4, 2]}, [2, 3, 4]),
    ({'user1': [3, 1, 2], 
      'user2': [5, 4]}, [1, 2, 3, 4, 5]),
    ({'user1': [1, 2, 4, 5],
      'user2': [6, 7, 8, 9],
      'user3': [10, 13, 18, 18]}, [1, 2, 4, 5, 6, 7, 8, 9, 10, 13, 18]),
    ({'user1': [0, 0, 0, 0, 1],
      'user2': [1, 1, 1, 1, 2],
      'user3': [2, 2, 2, 0]}, [0, 1, 2]),
    ({'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]}, [15, 35, 54, 98, 119, 213])
])
def test_sorted_list(data_input, expected_output):
    assert sorted_list(data_input) == expected_output

@pytest.mark.parametrize("data_input, expected_output", [
    ([], []),
    ([{'visit1': ['Москва', '']},
    {'visit2': ['Архангельск', '']},
    {'visit3': ['Москва', '']},
    {'visit4': ['Париж', '']},
    {'visit5': ['Лиссабон', '']},
    {'visit6': ['Курск', '']},
    {'visit7': ['Тула', '']},
    {'visit8': ['Владимир', '']},
    {'visit9': ['Дели', '']},
    {'visit10': ['Барселона', '']}], []),
    ([{'visit1': ['', 'Россия']},
    {'visit2': ['', 'Португалия']},
    {'visit3': ['', 'Франция']},
    {'visit4': ['', 'Португалия']},
    {'visit5': ['', 'Россия']},
    {'visit6': ['', 'Испания']},
    {'visit7': ['', 'Португалия']},
    {'visit8': ['', 'Россия']},
    {'visit9': ['', 'Испания']},
    {'visit10': ['', 'Россия']}], [{'visit1': ['', 'Россия']}, {'visit5': ['', 'Россия']}, {'visit8': ['', 'Россия']}, {'visit10': ['', 'Россия']}]),
    ([{'visit1': ['', '']},
    {'visit2': ['', '']},
    {'visit3': ['', '']},
    {'visit4': ['', '']},
    {'visit5': ['', '']},
    {'visit6': ['', '']},
    {'visit7': ['', '']},
    {'visit8': ['', '']},
    {'visit9': ['', '']},
    {'visit10': ['', '']}], []),
    ([{'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}], [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])
])
def test_filter_list_function(data_input, expected_output):
    assert filter_list_function(data_input) == expected_output

@pytest.mark.parametrize("data_input, expected_output", [
    ({}, ValueError),
    ({'facebook': 0, 'yandex': 0, 'vk': 0, 'google': 0, 'email': 0, 'ok': 0}, 'facebook'),
    ({'facebook': 1, 'yandex': 2, 'vk': 3, 'google': 4, 'email': 5, 'ok': 6}, 'ok'),
    ({'facebook': -1, 'yandex': -2, 'vk': -3, 'google': -4, 'email': -5, 'ok': -6}, 'facebook'),
    ({'facebook': 999, 'yandex': 998, 'vk': 998, 'google': 999, 'email': 998, 'ok': 999}, 'facebook'),
    ({'facebook': 10, 'yandex': 100, 'facebook': 20, 'facebook': 30, 'facebook': 40, 'facebook': 50}, 'yandex'),
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex')
])
def test_stats_function(data_input, expected_output):
    assert stats_function(data_input) == expected_output


@pytest.mark.parametrize("url, headers, params, expected_output", [
    ('https://cloud-api.yandex.net/v1/disk/resources', {'Authorization': get_token()}, {'path': 'TEST_FOLDER'}, 200),
    ('https://cloud-api.yandex.net/v1/disk/resources', {}, {'path': 'TEST_FOLDER'}, 200),
    ('https://cloud-api.yandex.net/v1/disk/resources', {'Authorization': get_token()}, {}, 200)
])
def test_create_folder(url, headers, params, expected_output):
    assert create_folder(url, headers, params) == expected_output

@pytest.mark.parametrize("url, headers, params, expected_output", [
    ('https://cloud-api.yandex.net/v1/disk/resources', {'Authorization': get_token()}, {'path': 'TEST_FOLDER'}, 200),
    ('https://cloud-api.yandex.net/v1/disk/resources', {'Authorization': get_token()}, {'path': 'TEST_FOLDER'}, 409)
])
def test_create_existing_folder(url, headers, params, expected_output):
    response = requests.put(url, headers=headers, params=params)
    assert response.status_code == expected_output
        