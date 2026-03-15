# SWEA - 7465
# 창용마을 무리의 개수

import sys
sys.stdin = open('chanyong.txt')

def dfs(idx):
    visited[idx] = True

    for i in lst[idx]:
        if not visited[i]:
            dfs(i)


    pass

TC = int(input())

for test_case in range(1, TC + 1):
    num, edge = map(int, input().split())
    # info = [list(map(int, input().split())) for _ in range(edge)]
    lst = [[] for _ in range(num + 1)]
    for _ in range(edge):
        e1, e2 = map(int, input().split())
        lst[e1].append(e2)
        lst[e2].append(e1)

    
    visited = [False for _ in range(num + 1)]

    count = 0
    for i in range(1, num+ 1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(f'#{test_case} {count}')