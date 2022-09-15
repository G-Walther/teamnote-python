from math import sqrt

def is_prime_number(x:int) -> bool:
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    elif x < 2:
        return False
    
    for i in range(3, int(sqrt(x)+1), 2):
        if x % i == 0:
            return False
    return True

def is_prime_number_simple(x: int) -> bool:
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
