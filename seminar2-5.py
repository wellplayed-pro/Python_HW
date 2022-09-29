import random

def get_list(n, left, right):
    return [random.randint(left, right) for i in range(n)]

def shuffle(lst):
    return random.shuffle(lst)

n = 10
left = -10
right = 20

list = get_list(n, left, right)
print(list)
shuffle(list)
print(list)