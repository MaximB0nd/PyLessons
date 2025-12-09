# Напиши функцию process_data(data), которая:
#
# Принимает список кортежей (id, value), где value может быть любого типа
# Возвращает словарь, где:
#
# Ключ: тип значения (как строка, например "int", "str")
# Значение: список уникальных id для этого типа

from collections import defaultdict

data = [
    (1, 100),
    (2, "hello"),
    (3, 3.14),
    (4, 200),
    (5, "world"),
    (6, "hello"),
    (7, 300)
]

def process_data(data):
    dictionary = {}
    for entry in data:
        dictionary[type(entry[1]).__name__] = dictionary.get(type(entry[1]).__name__, []) + [entry[0]]

    return dictionary


def another_process_data(data):
    dictionary = {}

    for id, value in data:
        type_of_value = type(value).__name__
        if type_of_value not in dictionary:
            dictionary[type_of_value] = {id}
        else:
            dictionary[type_of_value].add(id)

    return {k: sorted(v) for k, v in dictionary.items()}

def other_another_process_data(data):
    dictionary = defaultdict(set)
    for id, value in data:
        value_type = type(value).__name__
        dictionary[value_type].add(id)

    return {k: sorted(v) for k, v in dictionary.items()}

if __name__ == '__main__':
    print(process_data(data) == another_process_data(data) == other_another_process_data(data))