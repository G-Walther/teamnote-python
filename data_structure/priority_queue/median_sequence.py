import heapq
from typing import List

def median_sequence(seq:List[int]) -> List[int]:
    result = []
    lheap, rheap = [], []
    for x in seq:
        if len(lheap)==len(rheap):
            heapq.heappush(lheap, -x)
        else:
            heapq.heappush(rheap, x)
        if rheap and rheap[0] < -lheap[0]:
            l = -heapq.heappop(lheap)
            r = heapq.heappop(rheap)
            heapq.heappush(lheap, -r)
            heapq.heappush(rheap, l)
        result.append(-lheap[0])
    return result
