import sys

sys.stdin = open('swea-5102.txt')

def dfs(start_node, arrive_node, distance):
    # 글로벌 변수 설정 why? 함수 밖에서 변수를 조정할려고
    global min_val

    # 가지치기 why? 메모리 줄일려고
    if distance >= min_val:
        return

    # 도착시 최솟값 재할당 why? 도착했으니깐 값 재할당
    if start_node == arrive_node:
        min_val = min(min_val, distance)
        return

    for j in new[start_node]:
        if not visited[j]:
            # 방문처리 why? 왔던길 또 안올려고
            visited[j] = True
            dfs(j,arrive_node , distance +1)
            # 백트래킹 why? 이전으로 돌아가면 방문처리를 복구해야해서
            visited[j] = False



T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    
    # 1. 노드 연결 why 일단 이거를 만들어야지 돌아가니깐
    adj = [list(map(int, input().split())) for _ in range(E)]
    new = [[] for _ in range(V + 1)]

    # print(adj)
    for u, v in adj:
        new[u].append(v)
        new[v].append(u)

    S, G = map(int, input().split())
    cnt =0
    min_val = float('inf')
    visited = [False] * (V + 1) # 방문 배열 생성
    visited[S] = True
    # print(new)

# ===
# DFS
# ===
    # dfs 선택 why? 공부할려고
    dfs(S, G, cnt)
    if min_val != float('inf'):
        ans = min_val
    else:
        ans = 0

    print(ans)