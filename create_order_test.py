import sender_stand_request
import data


#  Команда на сохранение трека
def get_track(body):
    track_body = data.track_body.copy()
    track_resp = sender_stand_request.post_new_order(body)
    return track_resp.json()["track"]


def test_get_order_by_track():
    track = {"t":["track"]}

    assert sender_stand_request.response.status_code == 200
