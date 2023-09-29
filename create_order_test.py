import sender_stand_request
import data


#  Команда на сохранение трека


def test_get_order_by_track():
    response = sender_stand_request.post_new_order(data.order_body)


    assert response.status_code == 201


    response = sender_stand_request.get_order_by_track()


    assert response.status_code == 200

