import allure
import pytest

from data import ORDER_CASES
from steps import create_order


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ создаётся с вариантом цвета: {order_payload}')
    @pytest.mark.parametrize(
        'order_payload',
        ORDER_CASES,
        ids=['black', 'grey', 'black-and-grey', 'without-color']
    )
    def test_create_order_with_different_colors_success(
        self,
        order_payload,
        created_order_tracks
    ):
        response = create_order(order_payload.copy())

        assert response.status_code == 201

        track = response.json()['track']
        assert isinstance(track, int)
        created_order_tracks.append(track)
