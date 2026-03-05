# 나만의 언어
# 자료구조 알고리즘(최대한 자세히)
# 검증(시간복잡도 등등)

# 계획

# 두명이 서로 연결이 되었다는거는 패런츠 차일드 관계로 풀어야하나

# 


# 아 뭔가가 뭔가인데
# 먼가가 먼가 아쉽다 아쉬워
# 인접 리스트를 쓴다는것에서 일반 DFS랑은 다르다
# 이외에 내가 얻어갈게 있는가 하면 잘 모르겠다.
# 다른 방식을 또 풀어봐야지. 일단 과제 다하고
import sys

# DFS로 풀어야한다고 했던 판단 기준:
# 1. DFS 연습 할려고
# 2. BFS보다 효율적이라고 생각
def dfs(v):
    if visited[v]:
        return False
    
    visited[v] = True
    for next_node in relates[v]:
        dfs(next_node)

    return True

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    # 인접리스트 생성
    relates = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        # 인접리스트 append
        relates[u].append(v)
        relates[v].append(u)

    # 방문 처리
    visited = [False]  * (N +1)
    count = 0

    # dfs 탐색
    for i in range(1, N + 1):
        if dfs(i):
            count += 1

    print(f"#{tc} {count}")
