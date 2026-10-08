import allure
import requests

from urls import Urls


@allure.feature('Получение списка заказов')
class TestGetOrders:

    @allure.title('Ответ содержит список заказов')
    def test_get_orders_returns_orders_list(self):
        response = requests.get(Urls.ORDERS)

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)