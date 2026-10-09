import allure
import requests

from urls import Urls


@allure.step('Создать курьера')
def create_courier(courier_data):
    return requests.post(
        Urls.CREATE_COURIER,
        json=courier_data
    )


@allure.step('Авторизовать курьера')
def login_courier(login_data):
    return requests.post(
        Urls.LOGIN_COURIER,
        json=login_data
    )


@allure.step('Удалить курьера с идентификатором {courier_id}')
def delete_courier(courier_id):
    return requests.delete(
        f'{Urls.CREATE_COURIER}/{courier_id}'
    )


@allure.step('Создать заказ')
def create_order(order_data):
    return requests.post(
        Urls.ORDERS,
        json=order_data
    )


@allure.step('Отменить заказ с номером {track}')
def cancel_order(track):
    return requests.put(
        Urls.CANCEL_ORDER,
        params={'track': track}
    )


@allure.step('Получить список заказов')
def get_orders():
    return requests.get(Urls.ORDERS)