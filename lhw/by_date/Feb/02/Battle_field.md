# SWEA - 1873
# 상호의 배틀필드

- 매우 복잡하게 풀어낸 문제.. 일단 풀었으니 md를 작성하지만 추후 AI 에게 리팩토링을 요청해야 할 듯 합니다.

- 너무 복잡하니 코드를 다시 훑어보는 데에도 시간이 오래 걸렸습니다. 결국 변수 하나가 잘못 할당되어 있어서 테스트 케이스 98개중 68개만 통과하였고 문제점을 찾아내지 못한 채 AI 에게 검사를 요구했습니다.

- 우선 오래걸린 원인은 너무 많은 분기처리인데 아마 함수를 만들어도 좋을 듯 합니다. AI 리팩토링 결과도 추후 추가하겠습니다.

- 풀며 어려웠던 점은 이전 카드 정렬 문제와 비슷하게 리스트의 개념이었습니다. 저번에 얻었던 인사이트를 활용하고자 했지만 비슷한 부분에서 펑크가 나서 시간을 많이 사용했습니다.

- 리스트 안의 요소의 위치를 바꾸려 할 때 좌변과 우변을 설정하는데 최근 애를 먹고 있습니다. 예를 들면 이런 식입니다.
```python
if act == 'U':
    dx, dy = dir[3]
    if 0 <= px+dx < H and 0 <= py+dy < W:
        after = field[px+dx][py+dy]
        if after == '.': 
            position = (px+dx, py+dy) 
            field[px][py], field[px+dx][py+dy] = after, '^' # 둘이 교환
            current_tank_pos = field[px+dx][py+dy]
```
- 위 코드의 교환하는 부분에서 애를 먹었는데, 좌표를 할당한 변수의 값을 바꾸려고 계속 시도해서 안된 것이었습니다.

- 이전에 교환을 진행 할 때마다 새로 인덱스를 계산하는 문제를 개선하기 위해 변수를 도입한 것이었는데 이번에는 변수의 값은 변하지만 변수에 할당한 좌표의 값이 변하지 않는 게 문제였습니다. 코드를 수정하며 계속 기록을 지우다보니 설명하기 쉽게 코드가 남아있진 않습니다. 다음에는 문제가 되었던 부분은 따로 주석을 달아 기록해둬야겠습니다.


# 리팩토링 후기

- 약 170줄의 코드가 70줄 정도로 줄었습니다. 저는 분기처리를 했던 부분들을 다 dict 구조로 풀어냈습니다.

> U/D/L/R 4개 블록이 완전 하나로 합쳐짐

> S에서 위/아래/왼/오른쪽 for문 4개가 while 한 개로 합쳐짐

> current_tank_pos 변수 관리 실수가 사라짐 (field 안의 탱크 문자가 진실)

- 가져갈만한 인사이트는 dictionary 구조 활용 / while 문 활용 / 변수 최소화(실수 방지) 정도 인 듯 하고 두고두고 꺼내봐야겠습니다.

- 추가로 AI 코드의 위치 찾기 부분이 이해가 안가서 물어봤습니다.
> 

# AI 리팩토링 버전
```python
TC = int(input())

move_map = {
    'U': (-1, 0, '^'),
    'D': (1, 0, 'v'),
    'L': (0, -1, '<'),
    'R': (0, 1, '>'),
}

dir_map = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

for test_case in range(1, TC + 1):
    H, W = map(int, input().split())
    field = [list(input().strip()) for _ in range(H)]

    # 탱크 위치 찾기
    x = y = -1
    for i in range(H):
        for j in range(W):
            if field[i][j] in dir_map:
                x, y = i, j
                break
        if x != -1:
            break

    N = int(input())          # N은 사실 action 길이지만 입력 형식상 받기만
    action = input().strip()

    for act in action:
        # 이동/방향 전환
        if act in move_map:
            dx, dy, new_shape = move_map[act]

            # 1) 방향은 무조건 바뀜
            field[x][y] = new_shape

            # 2) 한 칸 이동 가능하면 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == '.':
                field[x][y] = '.'
                field[nx][ny] = new_shape
                x, y = nx, ny

        # 발사
        elif act == 'S':
            tank_shape = field[x][y]       # 현재 탱크 방향 문자
            dx, dy = dir_map[tank_shape]

            bx, by = x + dx, y + dy
            while 0 <= bx < H and 0 <= by < W:
                if field[bx][by] == '*':   # 벽돌
                    field[bx][by] = '.'
                    break
                if field[bx][by] == '#':   # 강철
                    break
                bx += dx
                by += dy

    print(f'#{test_case} ', end='')
    for row in field:
        print(''.join(row))

```

# 본 코드
```python
TC = int(input())

for test_case in range(1, TC+1):
    H, W = map(int, input().split()) # H * W 의 격자
    field = [list(map(str, input())) for _ in range(H)]

    # field.append(input() for _ in range(H)) # 필드 행렬

    # 방향 설정
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] # U, D, L, R 순

    for line in range(H): # 전차 위치 찾기 // 필드 해당 좌표 표시
        for tank in range(W):
            if field[line][tank] == '^':
                current_tank_pos = field[line][tank] # 해당 좌표 필드 컨디션
                position = (line, tank) # 전차 위치
                # position = (tank, line) # (y, x)에서 (x, y) 로 변환
                
            if field[line][tank] == 'v':
                current_tank_pos = field[line][tank]
                position = (line, tank)
                # position = (tank, line)

            if field[line][tank] == '<':
                current_tank_pos = field[line][tank]
                position = (line, tank)
                # position = (tank, line)
                
            if field[line][tank] == '>':
                current_tank_pos = field[line][tank] 
                position = (line, tank)
                # position = (tank, line)

            # line = 2 , tank = 1
            # field_condition = field[2][1]
            # position = (1, 2)
                
    N = int(input())
    action = input()
    px, py = position
    for act in action: # action 에서 하나씩 동작 수행
        # 동작마다 분기처리 ? U, D, L, R, S 5개
        # for act in action_string:
            (px, py) = position # line = px, tank = py

            if act == 'U':
                # 방향 설정 할 때 부호에 주의하자. 행렬상에서 위로 올라가는거기 때문에 앞에 죄표가 -가 되야 위로 올라감
                dx, dy = dir[3] # dx = 1, dy = 0
                if 0 <= px+dx < H and 0 <= py+dy < W: # 필드 밖으로 못나가도록
                    after = field[px+dx][py+dy] # field[px][py] 가 현재 포지션
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, '^' # 둘이 교환
                        # ax, ay = px+dx, py+dy
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = '^'
                        field[px][py] = '^' # 방향만 변경
                        continue
                else: # 가려는 곳이 필드 밖이면
                    current_tank_pos = '^'
                    field[px][py] = '^' # 방향만 변경
                    continue

            if act == 'D':
                dx, dy = dir[2]
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, 'v' # 둘이 교환
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = 'v'
                        field[px][py] = 'v'
                        continue
                else:
                    current_tank_pos = 'v'
                    field[px][py] = 'v'
                    continue

            if act == 'R':
                dx, dy = dir[0]
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, '>'
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = '>'
                        field[px][py] = '>'
                        continue
                else:
                    current_tank_pos = '>'
                    field[px][py] = '>'
                    continue

            if act == 'L':
                dx, dy = dir[1]
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, '<' # 둘이 교환
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = '<'
                        field[px][py] = '<'
                        continue
                else:
                    current_tank_pos = '<'
                    field[px][py] = '<'
                    continue

            # 이동 완료 // 검증 미완

            # 끝까지 쭉 이동한다.
            if act == 'S':
                # 현재 포지션 방향 따라 분기처리 '^', 'v', '>', '<'
                # 현재 포지션 befor == field[px][py]
                # x 축 포탄 이동거리는 W - py(오른쪽) or py(왼쪽)
                # y 축 포탄 이동거리는 H - px(아래) or px(위)
                # px 는 line, H이고 py는 tank, W 임에 주의
                current_tank_pos
                if current_tank_pos == '^':
                    for distance in range(1, px+1):
                        # 위쪽으로 필드 상태 확인
                        if field[px-distance][py] == '*': # 벽돌이면 파괴
                            field[px-distance][py] = '.'
                            break
                        elif field[px-distance][py] == '#': # 강철이면 continue
                            break
                        # 물이나 평지는 무시
                if current_tank_pos == 'v':
                    for distance in range(1, H-px): # H 4 , px 2 
                        # 아래쪽으로 필드 상태 확인
                        if field[px+distance][py] == '*': # 벽돌이면 파괴
                            field[px+distance][py] = '.'
                            break
                        elif field[px+distance][py] == '#': # 강철이면 continue
                            break

                if current_tank_pos == '>':
                    for distance in range(1, W-py):
                        # 오른쪽으로 필드 상태 확인
                        if field[px][py+distance] == '*': # 벽돌이면 파괴
                            field[px][py+distance] = '.'
                            break
                        elif field[px][py+distance] == '#': # 강철이면 continue
                            break

                if current_tank_pos == '<':
                    for distance in range(1, py+1):
                        # 왼쪽으로 필드 상태 확인
                        if field[px][py-distance] == '*': # 벽돌이면 파괴
                            field[px][py-distance] = '.'
                            break
                        elif field[px][py-distance] == '#': # 강철이면 continue
                            break                

    
    print(f'#{test_case} ',end='')
    for answer in field:
        print(''.join(answer))
```