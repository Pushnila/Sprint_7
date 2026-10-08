import allure
import pytest
import requests

from urls import Urls


@allure.feature('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Курьер может успешно авторизоваться')
    def test_login_courier_success(self, courier_data):
        requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

        login_payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        response = requests.post(
            Urls.LOGIN_COURIER,
            json=login_payload
        )

        assert response.status_code == 200
        assert isinstance(response.json().get('id'), int)

    @allure.title(
        'С пустым обязательным полем авторизация невозможна: {field}'
    )
    @pytest.mark.parametrize(
        'field',
        ['login', 'password'],
        ids=['without-login', 'without-password']
    )
    def test_login_without_required_field_returns_error(
        self,
        courier_data,
        field
    ):
        requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

        login_payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }
        login_payload[field] = ''

        response = requests.post(
            Urls.LOGIN_COURIER,
            json=login_payload
        )

        assert response.status_code == 400
        assert response.json()['message'] == (
            'Недостаточно данных для входа'
        )

    @allure.title(
        'Авторизация с неверным значением невозможна: {field}'
    )
    @pytest.mark.parametrize(
        'field',
        ['login', 'password'],
        ids=['wrong-login', 'wrong-password']
    )
    def test_login_with_wrong_credentials_returns_error(
        self,
        courier_data,
        field
    ):
        requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

        login_payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }
        login_payload[field] = f'wrong_{login_payload[field]}'

        response = requests.post(
            Urls.LOGIN_COURIER,
            json=login_payload
        )

        assert response.status_code == 404
        assert response.json()['message'] == (
            'Учетная запись не найдена'
        )

    @allure.title(
        'Несуществующий курьер не может авторизоваться'
    )
    def test_login_nonexistent_courier_returns_error(
        self,
        courier_data
    ):
        login_payload = {
            'login': courier_data['login'],
            'password': courier_data['password']
        }

        response = requests.post(
            Urls.LOGIN_COURIER,
            json=login_payload
        )

        assert response.status_code == 404
        assert response.json()['message'] == (
            'Учетная запись не найдена'
        )