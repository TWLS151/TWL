import sys
sys.stdin = open('swea_5102.txt')
from collections import deque

def bfs(S, G, V, adj_lst):
    q = deque([S])
    visited = [False] * (V + 1)
    distance = [0] * (V + 1)
    visited[S] = True
    while q:
        current_loc = q.popleft()
        if current_loc == G:
            return distance[current_loc]
        for num in adj_lst[current_loc]:
            if not visited[num]:
                visited[num] = True
                distance[num] = distance[current_loc] + 1
                q.append(num)
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1 , n2 = map(int, input().split())
        adj_lst[n1].append(n2)
        adj_lst[n2].append(n1)

    S,G = map(int, input().split())
    result = bfs(S, G, V, adj_lst)
    print(f'#{tc} {result}')