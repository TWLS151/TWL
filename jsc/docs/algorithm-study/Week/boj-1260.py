import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, w = map(int, input().split())
    # 이 아이디어가 좋다. 두개의 노드가 연결이 된것을 이차원 리스트를 만들고 그 안에 각 방에 append를 한다는 것이 인상적이었다.
    adj[u].append(w)
    adj[w].append(u)

for i in range(1, n + 1):
    # sort를 사용을 해서 숫자가 
    adj[i].sort()

visited_dfs = [False] * (n + 1)
visited_dfs = [False] * (n + 1)
