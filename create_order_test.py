import sender_stand_request
import data


#  Команда на сохранение трека
def test_get_order_by_track():
    response = sender_stand_request.post_new_order(data.order_body)

#  Получение ответа на запрос вывода заказа по треку
    response = sender_stand_request.get_order_by_track()

#  Проверка успешной обработки запроса на вывод заказа по треку
    assert response.status_code == 200
