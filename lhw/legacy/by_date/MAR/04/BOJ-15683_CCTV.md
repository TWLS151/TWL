# BOJ - 15683 _ 감시

### [1] 정의
```
브루트포스 DFS

[STATE]
1. IDX 번째까지 CCTV 방향이 정해진 상태 // 필드

[CHOICE]
1. 각 CCTV의 방향

[CONSTRAINT]
1. 방향은 십자형, 네 방향 뿐이다.
2. 벽은 넘어서 볼 수 없다
3. 다른 CCTV는 넘어서 볼 수 있다.

[CHANGE & ROLLBACK]
1. FIELD

[BASE]
1. idx == len(cctv)

[POURING]
1. 현재 필드의 사각 지대가 최소 크기보다 커지면 실패
2. 그럼 변화가 큰 값부터 계산을 하면 가지치기를 빠르게 할 수 있겠다.
3. CCTV 번호가 큰 IDX 부터 계산하자.
```


### [2] 코드
```python
dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

cd = [
    0,
    [[0], [1], [2], [3]],
    [(0, 1), (2, 3)],
    [(0, 3), (3, 1), (1, 2), (0, 2)],
    [(0, 2, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0)],
    [(0, 1, 2, 3)]
]

def dfs(idx, count):
    global cctv, max_checked, field
    
    # [BASE]
    # 끝까지 다 돌아보면 종료 및 감시구역 크기 갱신
    if idx == len(cctv):
        max_checked = max(max_checked, count)
        return
    
    # CHOICE & CONSTRAINT
    # 좌표와 CCTV 번호
    r, c, v = cctv[idx]
    
    for i in cd[v]:
        candidates = set()  # 백트래킹을 위한 집합
        for j in i:
            dr, dc = dirs[j]
            nr, nc = r+dr, c+dc

            # 필드를 나가거나 벽을 만나는 게 아니면 끝까지 간다
            while 0 <= nr < N and 0 <= nc < M and field[nr][nc] != 6:
                if field[nr][nc] == 0:  # 감시되고 있지 않은 빈 공간이면
                    candidates.add((nr, nc))  # 집합에 추가
                    field[nr][nc] = 7  # 필드에 표시
                nr, nc = nr+dr, nc+dc  # 진행
            
        dfs(idx+1, count+len(candidates))  # 재귀

        for a, b in candidates:  # 필드 백트래킹
            field[a][b] = 0


N, M = map(int, input().split())
field = []
cctv = []
zero_count = 0
for r in range(N):
    row = list(map(int, input().split()))
    field.append(row)
    for c in range(M):
        v = row[c]
        if 0 < v < 6:
            cctv.append((r, c, v))
        elif v == 0:
            zero_count += 1 


# 가지치기 위한 방문배열
visited = [[False] * M for _ in range(N)]  # 결국 사용 안함

# 가지치기를 위한 역순 정렬
cctv.sort(key=lambda x: -x[2])

max_checked = float('-inf')
dfs(0, 0)

print(zero_count - max_checked)
```
오랜만에 혼자 힘으로 해결한 문제입니다.  
잘했다고 생각하는 부분은 다음과 같습니다.
1. `가지치기`를 위해 `역순`으로 탐색한 점  
2. cd 리스트의 자료구조를 통일한 점  

가지치기를 깜빡하고 결국 진행하지는 않았지만 아이디어를 떠올린 점이 마음에 듭니다.  
그리고 다른 번호들과 달리 1번 CCTV 의 타입만 달라서 고민을 했었는데 이를 길이가 1인 리스트로 대체해서 코드를 단순화 했습니다.  
1번만 1차원 리스트 순회를 하고 나머지는 2차원 리스트 순회로 코드를 짜다가 영 아닌것 같아서 고민을 했다는 점과 해결책을 찾았다는 점도 만족스럽습니다.

### [3] AI 리팩터링
```python
# BOJ 15683 - 감시 (refactor keeping your approach)

import sys
input = sys.stdin.readline

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# CCTV type -> list of direction-sets
CCTV_DIRS = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [0, 2]],
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
    [[0, 1, 2, 3]],
]

def watch_line(board, r, c, d):
    """d 방향으로 쭉 보면서 새로 감시된 빈칸(0)을 7로 칠하고 그 좌표 목록 반환"""
    dr, dc = DIRS[d]
    nr, nc = r + dr, c + dc
    changed = []

    while 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 6:
        if board[nr][nc] == 0:
            board[nr][nc] = 7
            changed.append((nr, nc))
        nr += dr
        nc += dc

    return changed

def dfs(idx, watched):
    global best

    # (선택) 간단 가지치기: 지금까지 감시가 이미 최고면 계속, 아니라도 상한으로 컷 가능
    # 예: 남은 cctv가 최대한 0을 다 덮는다고 해도 best를 못 넘으면 컷
    # 여기서는 가볍게: watched가 best보다 작아도 계속 탐색(기본)

    if idx == len(cctvs):
        if watched > best:
            best = watched
        return

    r, c, typ = cctvs[idx]

    for dirset in CCTV_DIRS[typ]:
        changed_all = []
        # 현재 방향 세트 감시
        for d in dirset:
            changed_all.extend(watch_line(field, r, c, d))

        dfs(idx + 1, watched + len(changed_all))

        # rollback
        for x, y in changed_all:
            field[x][y] = 0

N, M = map(int, input().split())
field = []
cctvs = []
zeros = 0

for i in range(N):
    row = list(map(int, input().split()))
    field.append(row)
    for j, v in enumerate(row):
        if 1 <= v <= 5:
            cctvs.append((i, j, v))
        elif v == 0:
            zeros += 1

# 큰 CCTV부터(5,4,3,2,1) 하면 가지치기/수렴에 도움 되는 경우 많음
cctvs.sort(key=lambda x: -x[2])

best = 0
dfs(0, 0)

print(zeros - best)
```
가지치기를 설계하는 데 실패했어서 가지치기 파트가 눈여겨 볼 포인트입니다.

# [4] AI 정석 해설코드
```python
# BOJ 15683 - 감시 (canonical backtracking with rollback list)

import sys
input = sys.stdin.readline

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌로 두는 버전도 많음

TYPE_DIRS = [
    [],
    [[0], [1], [2], [3]],                 # 1
    [[0, 2], [1, 3]],                     # 2
    [[0, 1], [1, 2], [2, 3], [3, 0]],     # 3
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4
    [[0, 1, 2, 3]]                        # 5
]

def apply_watch(r, c, d):
    """한 방향 감시 적용: 새로 칠한 칸 좌표 리스트 반환"""
    dr, dc = DIRS[d]
    nr, nc = r + dr, c + dc
    changed = []
    while 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 6:
        if board[nr][nc] == 0:
            board[nr][nc] = 7
            changed.append((nr, nc))
        nr += dr
        nc += dc
    return changed

def backtrack(idx, covered):
    global best

    if idx == len(cameras):
        best = max(best, covered)
        return

    r, c, t = cameras[idx]
    for dirset in TYPE_DIRS[t]:
        changed_all = []
        for d in dirset:
            changed_all.extend(apply_watch(r, c, d))

        backtrack(idx + 1, covered + len(changed_all))

        for x, y in changed_all:
            board[x][y] = 0

N, M = map(int, input().split())
board = []
cameras = []
empty = 0

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j, v in enumerate(row):
        if 1 <= v <= 5:
            cameras.append((i, j, v))
        elif v == 0:
            empty += 1

# (선택) 큰 타입부터 -> 평균적으로 탐색이 빨라지는 편
cameras.sort(key=lambda x: -x[2])

best = 0
backtrack(0, 0)

print(empty - best)
```
AI 코드는 둘 다 enumerate() 함수를 이용한 부분이 인상 깊습니다. 다시 한 번 찬찬히 살펴보고 득이 커보이면 취해야겠습니다.