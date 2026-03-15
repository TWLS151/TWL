# BOJ - 11724
# 연결 요소의 개수

import sys
# sys.stdin = open('connection.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(node):

    visited[node] = True

    for child in adj_info[node]:
        if not visited[child]:
            dfs(child)

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
adj_info = [[] for _ in range(N + 1)]
for _ in range(M):
    p, c = map(int, input().split())
    adj_info[p].append(c)
    adj_info[c].append(p)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)