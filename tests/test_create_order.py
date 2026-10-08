import allure
import pytest
import requests

from data import ORDER_COLOR_CASES, ORDER_DATA
from urls import Urls


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ создаётся с вариантом цвета: {color}')
    @pytest.mark.parametrize(
        'color',
        ORDER_COLOR_CASES,
        ids=[
            'black',
            'grey',
            'black-and-grey',
            'without-color'
        ]
    )
    def test_create_order_with_different_colors_success(
        self,
        color,
        created_order_tracks
    ):
        order_payload = ORDER_DATA.copy()

        if color is not None:
            order_payload['color'] = color

        response = requests.post(
            Urls.ORDERS,
            json=order_payload
        )

        assert response.status_code == 201

        response_data = response.json()
        track = response_data.get('track')

        if track is not None:
            created_order_tracks.append(track)

        assert isinstance(track, int)