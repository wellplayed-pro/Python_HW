#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def input_numbers(x): 
    xy = ["x", "y"]
    a = []
    for i in range(x):
        reality = False
        while not reality:
            try:
                number = int(input(f"Введите координату {xy[i]}: "))
                a.append(number)
                reality = True
            except ValueError:
                print("Введенные данные не соответствую условиям")
    return a


def Length(a, b):  
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
    return lengthSegment


print("Введите координаты точки А")
A = input_numbers(2)
print("Введите координаты точки В")
B = input_numbers(2)

print(f"Длина отрезка: {round(Length(A, B),2)}")2