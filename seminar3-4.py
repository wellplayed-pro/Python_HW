#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number=int(input("Введите число "))
res = []
while number>0:
  res.append(number%2)
  number=number//2

print (*res, sep= "")