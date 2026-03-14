# BOJ - 2580  스도쿠

> 원본 코드
```python
import copy

N = 9

lst = []  # 0 좌표 리스트
board = []
for r in range(9):
    row = list(map(int, input().split()))
    for c in range(9):
        if row[c] == 0:
            lst.append((r, c))
    board.append(row)

# print(lst)
# print(board)
# 좌표마다 후보군 리스트 생성하고
# 확정되고 사용되면 전체에서 지운다


# 1. 해당 0 좌표에 들어갈 수 있는 후보 정리
# 2. 후보가 한 개인 좌표부터 채워나간다.

# 1-1. 함수를 만들어서 사전형에 넣어보자.
cand_info = {}

def cand(r, c):
    global cand_info
    # 가로
    rv = [False] * (N+1)
    for num in board[r]:
        rv[num] = True
    for idx in range(N+1):
        if rv[idx] == False:
            if (r, c) not in cand_info:
                cand_info[(r, c)] = set()
                cand_info[(r, c)].add(idx)
            else:
                cand_info[(r, c)].add(idx)

    # 세로
    cv = [False] * (N+1)
    for row in range(N):
        cv[board[row][c]] = True
    for idx in range(N+1):
        if cv[idx] == False:
            if (r, c) not in cand_info:
                cand_info[(r, c)] = set()
                cand_info[(r, c)].add(idx)
            else:
                cand_info[(r, c)].add(idx)
        
    pass

for r, c in lst:
    cand(r, c)  # 후보군 생성


# 구역 판별도 해야하는데 그냥 dfs 로 밀어붙여볼까

def dfs(board):
    global lst, cand_info

    # 기저조건
    # 조건 만족 못하면 종료

    # 반복
    # 하나 선택 후 다음 인덱스로
    for r, c in lst:
        for num in cand_info[(r, c)]:
            nboard = copy.deepcopy(board)
            board[r][c] = num

            dfs(board)

            board = copy.deepcopy(nboard)

    pass
```

코드를 작성하다가 백트래킹을 하는 과정에서 deepcopy를 선택했는데 작성하고 조금 생각해보니 무조건 터진다는 생각이 들어서 멈췄습니다.

백트래킹의 방식을 보드 전체가 아닌 변화가 있는 행만 선택해서 진행하는게 낫겠다는 생각을 했고 그러면 DFS 함수의 매개변수도 바꿔야한다는 곳까지 생각이 미치니 이 풀이는 실패했다는 생각이 들어 폐기했습니다.

가로, 세로 후보군을 생성하는 방식도 만들긴 했지만 썩 마음에 들지 않았고 9개 구역안에서 또 후보군을 추려야하니 손 댈 엄두도 나지 않았습니다.

# AI SOL.

> MAIN FEEDBACK
1. 교집합 아이디어 \
먼저 후보군을 찾는 방법이 좋지 못했습니다. 행, 열, 박스형 안에서 각각 가능한 모든 후보군을 모두 다 찾은 후 사전형에 추가했는데 `교집합` 아이디어를 활용하면 불필요한 일련의 과정들을 간소화 할 수 있었습니다.

1. 박스형 후보군 체크 \
총 아홉 개의 박스형 구역 안에서 후보군을 찾는 함수를 구현하려다가 좌표 특정에 실패했는데
이 두 줄로 구역을 특정할 수 있었습니다.
    ```
    sr = (r//3)*3
    sc = (c//3)*3
    ```

3. MRV Heuristic // MRV 휴리스틱 \
후보의 수가 가장 적은 위치부터 값을 확정해나가면 계산을 최소화 할 수 있겠다고 생각을 했습니다만 역시 구현에 실패했습니다.

1. 백트래킹 \
역시나 예상한 그대로 백트래킹의 방법이 잘못됐다는 피드백이 있었습니다.

\
다음은 AI의 코드이고 첫 번째는 원본의 특징을 살린 코드, 두 번째는 정석 해설 코드입니다.

```python
# FIRST CODE
import sys

N = 9
lst = []
board = []
for r in range(9):
    row = list(map(int, input().split()))
    for c in range(9):
        if row[c] == 0:
            lst.append((r, c))
    board.append(row)

def cand(r, c):
    used = set()

    # 가로
    used.update(board[r])
    # set.update()
    # 인자의 모든 요소를 집합에 추가한다.
    # .add() 는 하나의 요소, .update() 는 iterable 객체를 받음

    # 세로
    for rr in range(N):
        used.add(board[rr][c])
    
    # 박스
    sr = (r // 3) * 3
    sc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            used.add(board[sr + i][sc + j])

    # 사용된 적 없는 숫자들만 후보로 반환
    return {x for x in range(1, 10) if x not in used}

'''
후보를 찾기 위해 불리언 리스트를 만들고 모든 수를 확인 후 값이 False인 인덱스를
후보로 추가했었는데
이렇게 하니까 훨씬 간편하고 쉽게 진행됐다.

또한 가로 세로 박스형 모두 매우 간결하다.
'''

def dfs(idx):

    # 기저: 모든 칸 다 채움
    if idx == len(lst):
        for r in range(N):
            print(*board[r])
        sys.exit(0)

    r, c = lst[idx]
    # 후보군 생성
    candidates = cand(r, c)

    # 후보가 없으면 불가능한 가지
    if not candidates:
        return
    
    # 후보 하나씩 넣고 DFS 진행
    for num in candidates:
        board[r][c] = num
        dfs(idx+1)
        board[r][c] = 0

dfs(0)
```

```python
# SECOND CODE
import sys

N = 9
board = []
zeros = []

# 불리언 리스트 생성
row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

# 좌표의 구역 판별 함수
# 직관적으로 이해가 안된다.
# N-QUEEN 문제 때도 그렇고 아직 다차원 배열의 활용이 어렵다.
def box_id(r, c):
    return (r // 3)* 3 + (c // 3)

# 입력을 받고 동시에 불리언 리스트에 반영
for r in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for c in range(9):
        v = row[c]
        if v == 0:
            zeros.append((r, c))
        else:
            row_used[r][v] = True
            col_used[c][v] = True
            box_used[box_id(r, c)][v] = True

# 후보군 생성 함수
def get_candidates(r, c):
    b = box_id(r, c)
    res = []
    for num in range(1, 10):
        if not row_used[r][num] \
        and not col_used[c][num] \
        and not box_used[b][num]:
            res.append(num)
    return res

# DFS 함수
def dfs():

    # 기저: 더 이상 0이 없으면 성공 및 종료
    if not zeros:
        for r in range(9):
            print(*board[r])
        sys.exit(0)

    # MRV
    # 후보 개수가 최소인 칸을 선택
    best_i = -1
    best_cands = None

    # enumerate 함수를 이용해 인덱스와 값을 같이 추출
    for i, (r, c) in enumerate(zeros):
        # 후보군 생성
        cands = get_candidates(r, c)
        # 후보군이 없으면 안되는 분기이므로 종료
        if not cands:
            return
        # 수가 가장 적은 후보군을 갖는 위치를 찾기 위한 조건문
        if best_cands is None or len(cands) < len(best_cands):
            best_cands = cands
            best_i = i
            if len(best_cands) == 1:  # 후보가 한 개라면 바로 진행
                break

    # 위에서 찾은 최적의 인덱스를 사용
    r, c = zeros.pop(best_i)
    b = box_id(r, c)

    # 백트래킹 및 재귀
    for num in best_cands:
        board[r][c] = num
        row_used[r][num] = True
        col_used[c][num] = True
        box_used[b][num] = True

        dfs()

        row_used[r][num] = False
        col_used[c][num] = False
        box_used[b][num] = False

    zeros.insert(best_i, (r, c))

dfs()
```

### 개선점
최근 BOJ 기준 `실버 상위 ~ 골드 중상위` 정도의 `DFS`, `BFS`, `DP`, `시뮬에이션` 알고리즘 문제를 해결하고 있는데 쉽게 풀리는 문제도 왕왕 있지만 그렇지 않은 문제들을 분석해보면 항상 `상태 정의` 에서 무너지는 경향이 확인됩니다. 오늘 시도한 이 문제와 `N-QUEEN` 문제도 결국 `상태`가 불분명하니 구현에서 무너지는 패턴이었습니다. 결국 운이 좋게 상태 정의에 성공하면 해결하고 그렇지 않으면 실패하는 상황입니다.

AI 는 지금의 제가 `설계는 가능하지만 구현에서 흔들리는 상태` 라고 분석해줬습니다. 동시에 구현이 안정되면 급격히 성장할 수 있다는 낙관적인 말도 함께 말이죠. 하하, 이게.. 잘 모르겠네요.

참 생각이 많아지는 요즘입니다.