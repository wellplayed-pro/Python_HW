#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

with open('file.txt', 'w') as data:
  data.write('0\n')
  data.write('1\n')
  data.write('2\n')
  data.write('3\n')
  data.write('4\n')
  
def get_numbers(n):
    return [randint(-n, n) for i in range(-n, n + 1)]

def open_file_path(path):
  data = open (path, 'r')
  list = [int(line.strip()) for line in data]
  data.close()
  return list

def multiplication (numbers, datalist):
  mult=1
  for i in datalist:
    mult*=numbers[i]
  return mult

n=10
path= 'file.txt'
datalist=open_file_path(path)
numbers=get_numbers(n)

print (datalist)
print (numbers)
print (multiplication(numbers, datalist))
