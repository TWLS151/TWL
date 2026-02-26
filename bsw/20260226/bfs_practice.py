import sys
from collections import deque

sys.stdin = open('input.txt')
def bfs(start_loc, V, adj_lst):


    visited = [False] * (V + 1)
    q = deque()
    path = []

    visited[start_loc] == True
    q.append(start_loc)

    while q:
        current_loc = q.popleft()
        path.append(current_loc)
        for next_loc in sorted(adj_lst[current_loc]):
            if not visited[next_loc]:
                visited[next_loc] = True
                q.append(next_loc)
    return path


V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_lst = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

result_path = bfs(1, V, adj_lst)
print(''.join(map(str, result_path)))