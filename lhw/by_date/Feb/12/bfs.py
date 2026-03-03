import sys
from collections import deque

def bfs(start_node, V, adj_lst):
    visited = [False for _ in range(V + 1)]
    path = []
    q = deque()

    visited[start_node] = True
    q.append(start_node)

    while q:

        current_node = q.popleft()
        path.append(current_node)

        for next_node in sorted(adj_lst[current_node]):
            if not visited[next_node]:
                visited[current_node] = True
                q.append(next_node)

    return path




V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_lst = [[] for _ in range(V + 1)]
for i in range(E):
    p, c = data[i*2], data[i*2 + 1]
    adj_lst[p].append(c)
    adj_lst[c].append(p)

result_path = bfs(1, V, adj_lst)
print(''.join(map(str, result_path)))