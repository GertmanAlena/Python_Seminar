
from random import randint

def Random_Number(min_num:int, max_num:int, size:int):
    '''
    Returns array of current size with elements in range from min_num to max_num
    :params:
    min_num - start of range
    max_num - end of range
    size - length of array
    '''
    
    # rand_num = [randint(min_num, max_num) for i in range(size)]
    return [randint(min_num, max_num) for i in range(size)]

