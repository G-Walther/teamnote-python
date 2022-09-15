from typing import Set, Tuple

def sieve_of_eratosthenes(until:int) -> Tuple[Set[int]]:
    result, check = set([2]), [True]*(until+1)
    for i in range(3, until+1, 2):
        if check[i]:
            result.add(i)
        for j in range(i, until+1, i):
            check[j] = False
    return result
