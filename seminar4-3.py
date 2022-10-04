# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
my_list = [2, 3, 5, 9, 4, 3, 5, 6, 9, 8]
counter = {}

for elem in my_list:
    counter[elem] = counter.get(elem, 0) + 1

nodoubles = {element: count for element, count in counter.items() if count < 2}

print(nodoubles)