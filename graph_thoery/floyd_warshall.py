from typing import List

def floyd_warshall(graph:List[List[int]]):
    n = len(graph)
    for via in range(n):
        for start in range(n):
            for end in range(n):
                graph[start][end] = min(graph[start][end], graph[start][via]+graph[via][end])
