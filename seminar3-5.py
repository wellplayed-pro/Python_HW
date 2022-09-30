#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number=int(input("Введите число "))

def get_fibonacci(number):
    fibo_nums = []
    a, b = 1, 1
    for i in range(number):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (number+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(number)
print(get_fibonacci(number))
print(fibo_nums.index(0))