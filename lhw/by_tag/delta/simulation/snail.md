# SNAIL
## DELTA, SIMULATION

- 시뮬레이션 문제를 해결할 때 방향전환애 애를 먹는 경우가 있었습니다. 배틀필드 문제도 그랬고 이 문제도 그랬습니다.
- 그나마 배틀필드는 다른 변수가 하나 있어서 그에 맞게 하면 되었지만
- 이 달팽이는 조건이 달성되면 방향을 전환해야해서 까다로웠습니다.

```python
# 다음 위치가 유효한지(범위 내 + 빈칸) 확인
# 유효하지 않으면 방향 전환
if not (0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0):
    direction = (direction + 1) % 4  # 0->1->2->3->0... 순환
    # 바뀐 방향으로 다음 위치 다시 계산
    nx = x + dx[direction]
    ny = y + dy[direction]
```
- 그래서 이 청크를 봤을 때 조금은 알 것 같고 시원한 기분이 들었습니다.
- 나머지를 활용하는 방식이 이전부터 조금씩 눈에 띄긴 했지만 감흥이 없었는데 이번에는 좀 와닿았습니다.
- 계속 더하지만 4로 나눈 나머지의 값은 계속 순회하기 때문입니다.
- 특정 인덱스 안에서 반복하고 싶을 때 좋은 방법인 것 같습니다.


```python
TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    # 오른쪽, 아래, 왼쪽, 위 순서
    dir = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]
    # 모든 칸의 값은 현재 0
    # 이동 예정인 칸의 값이 0이면 num으로 교체
    # 0이 아니거나 필드 밖으로 나가면 우회전

    # 현재 위치 값 변수 생성 및 출발지 값 할당
    pos = [0, 0]
    arr[0][0] = 1

    # 각 위치에 할당할 변수 생성
    num = 1

    # 숫자 할당이 끝날때까지 전체 반복
    while num != N**2:
        # 큰 while 문이 끝날때까지 방향리스트 반복 순회
        for direction in dir:
            # 숫자 할당이 끝나면 반복문 탈출
            if num == N**2:
                break
            # 이미 숫자가 할당되어 있는 칸을 만나거나 필드 밖으로 나갈때 까지 반복하는 작은 반복문
            while num != N**2:
                # 전체 크기에 숫자 할당이 끝나면 작은 반복문 탈출
                if num == N**2:
                    break
                # 델타 계산을 위한 포지션의 좌표값과 방향의 좌표값 추출   
                px, py = pos
                dx, dy = direction
                # 필드 밖으로 나가지 않도록 하는 조건문
                if 0 <= px + dx < N and 0 <= py + dy < N:
                    # 숫자가 이미 할당되어 있는 칸을 만나면 작은 반복문 탈출
                    if arr[px + dx][py + dy] != 0:
                        break
                    # 다음 칸으로 진행할 수 있는 상태라고 판단되면 num + 1 후
                    num += 1
                    # 증가한 num 다음 칸에 할당
                    arr[px + dx][py + dy] = num
                    # 그리고 이동
                    pos = [px + dx, py + dy]
                # 필드 밖으로 나가면 방향 변경을 위해 작은 반복문 탈출
                else:
                    break

    # 출력
    print(f'#{test_case}')
    for i in range(N):
        print(f'{" ".join(map(str, arr[i]))}')
```