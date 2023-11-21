# EMPTY_CELL = " "
# def init_field(size: int, empty_cell: str = EMPTY_CELL):
#     return [[empty_cell] * size for i in range(size)]
#
# size = int(input('Введите число: '))
# #print(init_field(size, EMPTY_CELL))
#
# field = init_field(size, EMPTY_CELL)
#
# def draw_field(field):
#     for i in field:
#         print(i)
#
# draw_field(field)
#
# tuple = list(range(1, size * size + 1))
# print(tuple)
#
# text = input('Введите число: ')
# def get_int_val(text: str, border: tuple) -> int:
#
#     if text.isdigit():
#         if text in border:
#             number = int(text)
#             return number
# print(get_int_val(text, tuple))

def get_char_val(text: str, req_list: list) -> str:
    while text not in req_list:
        text = input('Введите строку: ')
    return text
print(get_char_val(text, req_list))




