import pytest

from helpers import generate_courier_data
from steps import (
    cancel_order,
    create_courier,
    delete_courier,
    login_courier
)


@pytest.fixture
def courier_data():
    data = generate_courier_data()

    yield data

    login_payload = {
        'login': data['login'],
        'password': data['password']
    }

    login_response = login_courier(login_payload)

    if login_response.status_code == 200:
        courier_id = login_response.json()['id']
        delete_courier(courier_id)


@pytest.fixture
def created_courier(courier_data):
    create_courier(courier_data)
    return courier_data


@pytest.fixture
def created_order_tracks():
    tracks = []

    yield tracks

    for track in tracks:
        cancel_order(track)
