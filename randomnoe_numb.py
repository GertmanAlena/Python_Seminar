
from random import randint


min = int(input('min ->: '))
max = int(input('max ->: '))
size = int(input('size ->: '))

def Random_Number(*params):
    rand_num = [randint(min, max) for i in range(size)]
    return rand_num

numbers = (Random_Number(min, max, size))