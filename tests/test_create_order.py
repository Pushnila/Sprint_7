import allure
import pytest

from data import ORDER_COLOR_CASES, ORDER_DATA
from steps import create_order


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ создаётся с вариантом цвета: {color}')
    @pytest.mark.parametrize(
        'color',
        ORDER_COLOR_CASES,
        ids=['black', 'grey', 'black-and-grey', 'without-color']
    )
    def test_create_order_with_different_colors_success(
        self,
        color,
        created_order_tracks
    ):
        order_payload = ORDER_DATA.copy()

        if color is not None:
            order_payload['color'] = color

        response = create_order(order_payload)

        assert response.status_code == 201

        track = response.json().get('track')
        if track is not None:
            created_order_tracks.append(track)

        assert isinstance(track, int)