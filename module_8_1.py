"""Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float),
так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой),
то возвращать строковое представление этих двух данных вместе (в том же порядке).
Во всех остальных случаях выполнять стандартные действия."""

def add_everything_up(arg_1, arg_2):
    try:
        rez = arg_1 + arg_2
    except TypeError:
        rez = str(arg_1) + str(arg_2)
        return rez
    else:
        if type(rez) == int or type(rez) == float:
            return round(rez, 3)
        else:
            return rez

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('конь', ' в яблоках'))
