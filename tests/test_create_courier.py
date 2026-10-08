import allure
import pytest
import requests

from urls import Urls


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно успешно создать')
    def test_create_courier_success(self, courier_data):
        response = requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier_returns_error(
        self,
        courier_data
    ):
        first_response = requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )
        second_response = requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()['message'] == (
            'Этот логин уже используется. Попробуйте другой.'
        )

    @allure.title(
        'Без обязательного поля создание курьера невозможно: {field}'
    )
    @pytest.mark.parametrize(
        'field',
        ['login', 'password'],
        ids=['without-login', 'without-password']
    )
    def test_create_courier_without_required_field_returns_error(
        self,
        courier_data,
        field
    ):
        incomplete_data = courier_data.copy()
        incomplete_data.pop(field)

        response = requests.post(
            Urls.CREATE_COURIER,
            json=incomplete_data
        )

        assert response.status_code == 400
        assert response.json()['message'] == (
            'Недостаточно данных для создания учетной записи'
        )