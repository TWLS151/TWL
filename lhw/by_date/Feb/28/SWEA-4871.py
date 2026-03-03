# SWEA - 4871
# 그래프 경로

import sys
sys.stdin = open('input.txt')

def dfs(s, g):
    global found

    if s == g:
        found = 1
        return
    
    visited[s] = True
    for i in adj[s]:
        if not visited[i] and found == 0:
            dfs(i, g)



TC = int(input())
for test_case in range(1, TC+1):
    V, E = map(int, input().split())
    visited = [False] * (V+1)

    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        p, c = map(int, input().split())
        adj[p].append(c)

    S, G = map(int, input().split())
    found = 0
    dfs(S, G)

    print(f'#{test_case} {found}')
    # print(adj)

    