import sys

# 파일 입력 설정
sys.stdin = open('03dfs.txt', 'r')

def dfs(num):
    visited[num] = True
    path.append(str(num))  # 방문한 노드를 경로 리스트에 추가

    # 인접 노드들을 작은 번호부터 방문 (예시 출력 순서 맞춤)
    for next_node in sorted(adj[num]):
        if not visited[next_node]:
            dfs(next_node)
    
    # 모든 탐색이 끝나면 True 반환
    return True

# 1. 데이터 읽기 (7 8 읽기)
try:
    line1 = input().split()
    if not line1: exit() # 빈 줄 예외 처리
    N, E = map(int, line1)

    # 2. 간선 정보 읽기
    edge_input = list(map(int, input().split()))
except EOFError:
    pass

# 3. 인접 리스트 초기화
adj = [[] for _ in range(N + 1)]

# 4. 그래프 구성 (무방향)
for i in range(E):
    n1, n2 = edge_input[i * 2], edge_input[i * 2 + 1]
    adj[n1].append(n2)
    adj[n2].append(n1)

visited = [False] * (N + 1)
path = []

# 5. 요청하신 'if dfs(1):' 구조로 출력
if dfs(1):
    print("-".join(path))