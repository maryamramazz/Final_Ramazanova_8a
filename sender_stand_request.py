import requests
import configuration
import data


# 1 - Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_URL,
                         json=body,
                         headers=data.headers)


# Команда для вывода ответа с треком и статус кодом
response = post_new_order(data.track_value)
track = response.json()["track"]
print(response.status_code)
print(response.json()["track"])
print(track)


#  Зарос к API на получение заказа по треку
def get_order_by_track():
    resp = post_new_order(data.order_body)
    #  Команда для приведения значения трэка к типу Строка
    track_value = str(resp.json()["track"])
    headers_param = data.headers.copy()
    headers_param["track"] = track_value

    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_TRACK + "?t=" + track_value)


# Команда для вывода ответа с статус кодом
response = get_order_by_track()
print(response.json())
# print(response.status_code)
