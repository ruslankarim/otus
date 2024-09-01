import random
import sys


def lizt():
    # Создаем пустой список
    my_list = []
    print(f'List before fill: {sys.getsizeof(my_list)}')

    # Заполняем список 1000000 случайными значениями
    for _ in range(10):
        my_list.append(random.randint(1, 100))  # Генерируем случайное значение от 1 до 100

    print(f'after fill 10: {sys.getsizeof(my_list)}')

    for _ in range(100):
        my_list.append(random.randint(1, 100))  # Генерируем случайное значение от 1 до 100

    print(f'after fill 100: {sys.getsizeof(my_list)}')

    for _ in range(1000):
        my_list.append(random.randint(1, 100))  # Генерируем случайное значение от 1 до 100

    print(f'after fill 1000: {sys.getsizeof(my_list)}')

    for _ in range(1000000):
        my_list.append(random.randint(1, 100))  # Генерируем случайное значение от 1 до 100

    print(f'after fill 1000000: {sys.getsizeof(my_list)}')


def tuble():
    # # Создаем пустой список
    # my_tuple = ()
    # print(f'Tuple before fill: {sys.getsizeof(my_tuple)}')
    #
    # # Заполняем список 1000000 случайными значениями
    # for _ in range(10):
    #     my_tuple += (random.randint(1, 100),)  # Генерируем случайное значение от 1 до 100
    #
    # print(f'after fill 10: {sys.getsizeof(my_tuple)}')
    #
    # for _ in range(100):
    #     my_tuple += (random.randint(1, 100),)  # Генерируем случайное значение от 1 до 100
    #
    # print(f'after fill 100: {sys.getsizeof(my_tuple)}')
    #
    # for _ in range(1000):
    #     my_tuple += (random.randint(1, 100),)  # Генерируем случайное значение от 1 до 100
    #
    # print(f'after fill 1000: {sys.getsizeof(my_tuple)}')
    #
    # for _ in range(1000000):
    #     my_tuple += (random.randint(1, 100),)  # Генерируем случайное значение от 1 до 100
    #
    # print(f'after fill 1000000: {sys.getsizeof(my_tuple)}')
    # t = ("past", "present", "future")
    # # t(1) = "present simple"
    # t[1: 1] = "present simple"
    # print(f't: {t}')
    a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1:: 3]
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')


def list_operation():
    a = [1, 2, 3, 4, 5]
    print(f'a: {a}')

    # a[2] = []
    # print(f'a[2] = []: {a}')

    # a[2:2] = []
    # print(f'a[2:2] = []: {a}')

    # a[2:3] = []
    # print(f'a[2:3] = []: {a}')

    # print(f'a: {a}')
    # a.remove(3)
    # print(f'a.remove(3): {a}')

    # a[-1:] = [6, 7]
    # print(f'a[-1:] = [6, 7]: {a}')

    # a.extend([6, 7])
    # print(f'a.extend([6, 7]): {a}')

    # a += [6, 7]
    # print(f'a += [6, 7]: {a}')

    # a.append([6, 7])
    # print(f'a.append([6, 7]): {a}')


# list_operation()
# lizt()
# tuble()

def mapping():
    pass
    # d = dict(foo=100, bar=200, baz=300)
    # d = {('foo', 100), ('bar', 200), ('baz', 300)}
    # d = {'foo': 100, 'bar': 200, 'baz': 300}
    # d = dict([('foo', 100), ('bar', 200), ('baz', 300)])
    # d = {(3+2j): ""}
    # d = {(1, [], 2): ""}
    # print(f'd: {d}')


mapping()
