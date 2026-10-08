import pytest
import requests

from helpers import generate_courier_data
from urls import Urls


@pytest.fixture
def courier_data():
    data = generate_courier_data()

    yield data

    login_payload = {
        'login': data['login'],
        'password': data['password']
    }

    login_response = requests.post(
        Urls.LOGIN_COURIER,
        json=login_payload
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()['id']

        requests.delete(
            f'{Urls.CREATE_COURIER}/{courier_id}'
        )


@pytest.fixture
def created_order_tracks():
    tracks = []

    yield tracks

    for track in tracks:
        requests.put(
            Urls.CANCEL_ORDER,
            params={'track': track}
        )