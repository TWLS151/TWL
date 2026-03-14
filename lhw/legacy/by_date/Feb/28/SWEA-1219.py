# SWEA - 1219
# 길찾기
# DFS

A = 0
B = 99

# import sys
# sys.stdin = open('input.txt')

# 이진트리
def dfs(a):
    global can

    if a == B:
        can = 1
        return
    
    visited[a] = True

    for i in adj[a]:
        if not visited[i] and can == 0:
            dfs(i)

    pass

for _ in range(1, 11):
    test_case, E = map(int, input().split())
    info = list(map(int, input().split()))
    visited = [False] * 100

    adj = [[] for _ in range(100)]
    for idx in range(E):
        p, c = info[idx*2], info[idx*2 + 1]
        adj[p].append(c)

    # A 에서 시작 B 까지

    can = 0
    dfs(A)

    print(f'#{test_case} {can}')
    