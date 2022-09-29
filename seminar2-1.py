#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

float_number=input()
sum=0
for i in float_number:
  if i !='.' and i!=',':
    sum += int(i)

print("Сумма цифр равна", sum)