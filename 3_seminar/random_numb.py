
from random import randint

def Random_Number(*params):
    min = int(input('min ->: '))
    max = int(input('max ->: '))
    size = int(input('size ->: '))
    rand_num = [randint(min, max) for i in range(size)]
    return rand_num

