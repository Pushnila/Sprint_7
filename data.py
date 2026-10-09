ORDER_DATA = {
    'firstName': 'Владислав',
    'lastName': 'Максимов',
    'address': 'Москва, улица Тестовая, дом 1',
    'metroStation': 4,
    'phone': '+7 999 123 45 67',
    'rentTime': 3,
    'deliveryDate': '2030-01-01',
    'comment': 'Позвонить перед доставкой'
}


COURIER_ALREADY_EXISTS_MESSAGE = (
    'Этот логин уже используется. Попробуйте другой.'
)
COURIER_REQUIRED_DATA_MESSAGE = (
    'Недостаточно данных для создания учетной записи'
)


ORDER_CASES = [
    {**ORDER_DATA, 'color': ['BLACK']},
    {**ORDER_DATA, 'color': ['GREY']},
    {**ORDER_DATA, 'color': ['BLACK', 'GREY']},
    ORDER_DATA.copy()
]
