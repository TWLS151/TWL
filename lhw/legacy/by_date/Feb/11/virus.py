# BOJ - 2606
# 바이러스

import sys
sys.stdin = open('virus.txt')

def dfs(node):

    size[node] = 1
    visited[node] = True

    for i in adj_info[node]:
        if not visited[i]:
            dfs(i)
            size[node] += size[i]

V = int(input())
E = int(input())
visited = [False] * (V+1)
adj_info = [[] for _ in range(V+1)]

for _ in range(E):
    p, c = map(int, input().split())
    adj_info[p].append(c)
    adj_info[c].append(p)

# 다 집어 넣었으니 재귀 함수 만들어야지
# 만들었으니 숫자 세야지

size = [0] * (V + 1)

dfs(1)

print(size[1] - 1)