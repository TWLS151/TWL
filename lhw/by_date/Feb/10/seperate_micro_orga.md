# SWEA - 2382
## 미생물 격리

- 많은 걸 배울 수 있는 문제였습니다.
1. `딕셔너리의 키값에 좌표를 넣을 수 있다.`
   - 처음에 문제를 보고 좌표를 key값으로 하고 value 값으로 정보를 넣으면 되겠다. 까지는 생각했으나 key 값으로 넣을만한 문자가 주어지지 않아서(알파벳 같은) 딕셔너리가 아니라 리스트로 문제를 풀이하기 시작했습니다. 그런데 리스트는 딕셔너리와 달리 동시 이동이 불가능합니다. 물론 리스트를 여러개 사용한다면 가능하겠지만 딕셔너리와 같은 효율은 나오지 않겠죠.
2. `방향 전환 변수의 설정`
    - 밑에 코드를 작성하겠지만 rev 라는 변수를 설정함으로서 방향 전환을 원하는 로직에 맞춰서 할 수 있다는 걸 알았습니다. 문제에서는 특정 구역에 진입하면 진행 방향을 역으로 바꾸라고 요구합니다. 저는 이걸 구현하기 위해 방향값을 언패킹하고 음수를 먹인 후 다시 패킹했는데 추가 변수를 하나 활용하면 그냥 방향값을 인덱스로 rev 변수에 집어 넣음으로서 순식간에 방향을 역으로 바꿀 수 있습니다.
3. `인덱스 활용`
    - 이 부분은 아직 글로 설명이 잘 안됩니다만 밑의 코드에서 객체의 정보를 순서대로 저장한 뒤 딕셔너리에 좌표와 인덱스값을 키밸류로 매칭합니다. 그럼 딕셔너리에 좌표를 넣으면 해당 좌표의 정보가 들어있는 인덱스를 반환하고 그 인덱스를 리스트에 넣으면 그 객체의 정보가 나열되는 형식입니다. 이 개념을 잘 이해하고 활용한다면 더 효율적인 작업이 가능할 것 같습니다.

- 개인적으로 이제 슬슬 로직을 짜는 것 보다는 그 로직을 구현하는데에 어려움이 느껴집니다. 시간이 지나고 경험이 쌓이면 해결될 문제라고 생각은 하지만 초조한 마음이 드는건 어쩔 수 없나봅니다. 조금 더 열심히 해야겠다는 생각이 듭니다.

### 주요 로직 및 코드 & 하단부 해설 코드
- 본인 코드
```python
# 미생물은 지정된 방향으로 한 시간에 한 칸씩 이동하고
# 경계에 닿으면 (n - 1) 그 수가 2로 나눈 몫 만큼 남는다
# 따라서 한 마리가 경계에 닿으면 군집이 사라진다.
# 이동 후 군집끼리 닿으면 둘이 합쳐진다.
# 합쳐지면 이동방향은 미생물 수가 많았던 군집의 방향이 된다.
# 미생물의 수가 같은 경우는 없다.
# 경계에 닿으면 이동 방향은 반대가 된다.
# 이동이 완료되었을 때 위치가 같으면 합쳐진다. 이동 도중은 고려하지 않는다.

# 0 배열을 만들고 배열에 딕셔너리를 매기면 되지 않을까?
# 딕셔너리 하나 하고 배열에 키 먹이면 될 거 같은데
# 경계에 들어가면 방향 바꾸고..
# key: ['dirs', 'nums'] 로 가볼까 그럼
# dict[key][0] = 방향
# dict[key][1] = 미생물 수
# 위치가 알파벳으로 주어지는 줄 알았는데 그냥 좌표만 주어지는구나
# 그럼 딕셔너리는 못 쓸 것 같고 그냥 좌표에다가 방향이랑 숫자 리스트를 박아야겠다.
# 근데 그러면 삼중 리스트가 되는데..
# 일단 해볼까

dirs = [0, 
    (0, 1), (-1, 0), (1, 0), (0, -1)
] # 문제에서 우상하좌 순으로 제시
# 1이 우라서 그냥 더미 0 하나 앞에 추가

TC = int(input())

for test_case in range(1, TC+1):
    pass
    size, time, zerg = map(int, input().split())
    matrix = [[0] * size for _ in range(size)]
    
    position = []
    for ameba in range(zerg):
        row, col, num, direction = map(int, input().split())
        position.append((row, col))
        matrix[row][col] = [direction, num]


    # 다중 객체를 시뮬레이션 할 떄는 포지션을 절대 인덱스로 받아야 하는 것 같다.
    for t in range(1, time+1):
        # for row, col in position:
        count = 0
        # for pos in range(len(position)):
        while count < len(position):
            # 이렇게 꺼내오면 나중에 위치가 변했을 때 갱신하기가 편하다
            row, col = position[count]
            # [0]이 방향 [1]이 숫자
            dr, dc = dirs[matrix[row][col][0]]
            nr, nc = row + dr, col + dc
            if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
                matrix[row][col][1] = matrix[row][col][1] // 2
                dr, dc = dirs[matrix[row][col][0]]
                matrix[row][col][0] = dirs.index((-dr, -dc)) 

            # 경계에 닿는 걸 먼저 처리해야하나본데
            # 경계 범위는 어떻게 되지?
            # 일단 row = 0, col = 0
            # row = size-1 col = size-1
            # 이렇게네
            # 이 안에 들어가면 방향 반대고 수 // 2
            # if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
            #     # 일단 수 절반
            #     # 이동하기 전에 줄여야겠다
            #     # matrix[nr][nc][1] //= 2
            #     matrix[row][col][1] //= 2
            #     # 이제 방향
            #     # matrix[nr][nc][0] = (matrix[nr][nc][0] + 2) %4 + 1
            #     # 그냥 음수 먹이면 되네
            #     # matrix[nr][nc][0] = -matrix[nr][nc][0]
            #     # 반대됐다.
            #     # 안된다.
            #     # 그냥 분기를 두개로 나누자 # 귀찮아 # 언패킹해서 음수 먹여
            #     dr, dc = dirs[matrix[row][col][0]]
            #     # 이렇게 가면 어떤데?
            #     dirs[matrix[nr][nc][0]] = dirs.index((-dr, -dc))

            # 이동하며 숫자 이동
            # 이동한 자리에 다른 군집이 있는지도 봐야하네, 추가하자
            if matrix[nr][nc] == 0:
                matrix[nr][nc] = matrix[row][col]
                
                # 경계 처리를 여기다가 해야하네
                # if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
                #     matrix[nr][nc][1] //= 2
                #     dr, dc = dirs[matrix[row][col][0]]
                #     matrix[nr][nc][0] = dirs.index((-dr, -dc)) 

                # 원래 있던 자리 숫자 0
                position[count] = (nr, nc)
                matrix[row][col] = 0
                count += 1
                # if (row, col) in position:
                #     position.remove((row, col))
                    
            else: # 이미 다른 군집이 있으면 합쳐야해
                # 숫자 비교부터 해야겠네
                # 숫자는 합치고 방향은 더 큰쪽 방향으로
                    # 여기서 처리하면 되네.
                    # 이미 군집이 있으면 포지션에도 좌표가 있어야하는데..
                    # 이동해서 온거면 없어도 되는구나
                    # 와 미치겠네
                    # 이동 표시도 해야하나본데  # 그냥 움직일때마다 위치를 갱신하는게 낫다
                
                # 먼저 와 있던 군집이 있으면 
                # 1. 누가 더 큰지 판단한다.
                # 2. 더 큰쪽을 살리고 더 작은 쪽의 숫자만 더 큰쪽에 추가한다.
                # 3. 좌표를 수정한다.
                # 4. 좌표를 set으로 관리하면? 좋은데.. 해보자 // 실패


                if matrix[nr][nc][1] < matrix[row][col][1]:
                    matrix[nr][nc][1] += matrix[row][col][1]
                    matrix[nr][nc][0] = matrix[row][col][0]
                else:
                    # else 처리 필요한가? 필요하네
                    matrix[nr][nc][1] += matrix[row][col][1]
                    # 방향은 그대로
                position[count] = (nr, nc)
                matrix[row][col] = 0
                count += 1

                # 다짰나?
    # nums =    # 지금 위치가 갱신이 안되고 있잖아?
                # 포지션 값이 계속 그대일 것 같은데
                # after_position 을 하나 만들까
                # 그리고 포지션 불러올때마다 갱신
    # time for문 끝나면 숫자 다 종합을 해야하는뎅
    total = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 0:
                continue
            else:
                total += matrix[row][col][1]

    print(f'#{test_case} {total}')
```
- 해설 코드 (주석은 제가 작성해서 정확하지 않을 수 있습니다.)
```python
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    A = []
    for _ in range(K):
        A.append(list(map(int, input().split())))

    for _ in range(M):
        info = dict()
        for row in range(K):
            r, c, k, d = A[row]
            # k = 미생물 수, 미생물 수가 0이면 다음 인덱스로
            if not k:
                continue
            # 이동할 좌표 설정
            nr = r + dr[d]
            nc = c + dc[d]
            # 이동
            A[row][0], A[row][1] = nr, nc
            # 이동한 곳이 경계라면
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                # 수는 절반으로 방향은 반대로
                A[row][2] //= 2
                A[row][3] = rev[d]
            # 이동한 좌표에 아무것도 없다면
            if (nr, nc) not in info.keys():
                # 그냥 이동
                info[(nr, nc)] = [row, k]
            # 뭔가 있으면
            else:
                # 그 지점의 위치와 미생물의 수를 확인
                num, size = info[(nr, nc)]
                # 새로 오는 군집과 수를 비교, 새로 오는 녀석이 더 크면
                if A[row][2] > size:
                    # 정보 갱신, 수와 방향을 새로 오는 녀석의 것으로
                    info[(nr, nc)] = [row, A[row][2]]
                    # 그 후 수를 합치고
                    A[row][2] += A[num][2]
                    # 병합된 미생물의 수 정보를 0으로 갱신
                    A[num][2] = 0
                # 새로 오는 놈이 더 작으면
                else:
                    # 반대로, 방향은 그대로
                    A[num][2] += A[row][2]
                    A[row][2] = 0
    # 총 수 변수
    microbe = 0
    # 리스트를 순회하며
    for m in A:
        # 미생물 수만 종합
        microbe += m[2]
    print("#{} {}".format(tc+1, microbe))
```