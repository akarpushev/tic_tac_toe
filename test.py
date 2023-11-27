EMPTY_CELL = " "
def init_field(size: int, empty_cell: str = EMPTY_CELL):
    """
    Создаёт и возвращет пустое поле для игры

    :param size: размер поля
    :param empty_cell: чем заполняется пустая ячейка
    :return: отображение пустого поля в виде листа листов

    """
    # TODO Можно выбрать своё представление поля, допустим строковое или одномерный список
    return [[empty_cell] * size for _ in range(size)]
print(init_field(4))

board = list(range(1, 10))
def draw_field(field):
    """
    Функция рисует поле
    :param field: Объект поля
    :return: None
    """
    for i in range(4):
        print(("|", EMPTY_CELL, "|") * i)

draw_field(board)

# def get_int_val(text: str, border: tuple[1, 9] = None) -> int:
#     num = input('Введите номер клетки: ')
#     while num not in tuple:
#         print('Введите число заново')
#     return num


    """
    Проверяет и возвращает число (это может быть необходимо когда вы хотите проверить,
        что пользователь ввел именно число и это число лежит в диапазоне border[0] и border[1]).
        Спрашиваем у пользователя ввод числа с текстом text и проверяем что оно соответствует требованиям, если не
        соответствует хотя бы одному требованию, то заново просим ввести число.

    :param text: Текст перед получением числа
    :param border: Ограничение на число (минимум, максимум)
    :return: Возвращает число, которое ввёл пользователь и прошедшее все проверки
    """
    # TODO Написать реализацию

    #return



