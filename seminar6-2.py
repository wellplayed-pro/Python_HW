# Задание 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

import Func_list_generation as lg
numbers_list = lg.list_generation()
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')4