## delta 이동

### 01_Delta

- NxN 크기의 2차원 배열에서 모든 원소의 인근값의 차(절대값)의 총합을 구하는 문제
- 절대값 구하기 : 1.abs, 2.if-else, 3.max-min

```python
T = int(input())

# 델타 검색을 위한 배열입니다.
# 순서대로 상, 하, 좌, 우 방향을 나타냅니다.
dr = [-1, 1, 0, 0]  # 행(row)의 변화량 (상, 하)
dc = [0, 0, -1, 1]  # 열(column)의 변화량 (좌, 우)

# 각 테스트 케이스에 대해 반복
for tc in range(1, T + 1):
    N = int(input())
    # N개의 줄에 걸쳐 N x N 크기의 2차원 배열(arr)을 입력받습니다.
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 차이 값의 총합을 저장할 변수를 0으로 초기화합니다.
    result = 0

    # 2차원 배열의 모든 요소를 순회하기 위한 중첩 반복문입니다.
    # r은 행 인덱스, c는 열 인덱스를 나타냅니다.
    # 이 두 반복문은 요소의 이동을 위한 반복문입니다.
    for r in range(N):
        for c in range(N):
            # 이 반복문은 탐색을 위한 반복문입니다.
            # 현재 위치 (r, c)의 상하좌우 인접 요소를 확인하기 위한 반복문입니다.
            for i in range(4):
                # 델타 값을 이용하여 인접한 칸의 좌표(nr, nc)를 계산합니다.
                nr = r + dr[i]
                nc = c + dc[i]

                # 계산된 인접 칸의 좌표가 배열의 경계를 벗어나는 경우는 계산에서 제외합니다.
                if 0 <= nr < N and 0 <= nc < N:
                    # 현재 칸의 값과 인접한 칸의 값의 차이의 절댓값을 구해 result에 더합니다.
                    # 1. abs 사용
                    # result += abs(arr[nr][nc] - arr[r][c])
                    # 2. if문 사용
                    if arr[nr][nc] >= arr[r][c]:
                        result += arr[nr][nc] - arr[r][c]
                    else: 
                        result += arr[n][c] - arr[nr][nc]
                    # 3. min-max 사용
                    # result += max(arr[nr][nc], arr[r][c]) - min(arr[nr][nc], arr[r][c])

    print(f'#{tc} {result}')
```