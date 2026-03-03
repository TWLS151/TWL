import sys
sys.stdin = open('input.txt')


# 디저트 카페

directions = [
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]

def func(r, c, cafe, d, cafes):
    global count

    # 시작점으로 돌아오면 종료
    if d == 3 and r == row and c == col and cafes >= 4:
        count = max(count, cafes)
        return
    # 방향부터
    for dirs in (d, d + 1):
        if dirs >= 4:
            continue
        
        dr, dc = directions[dirs]
        nr, nc = r + dr, c + dc

        if nr == row and nc == col and dirs == 3 and cafes >= 3:
            func(nr, nc, cafe, dirs, cafes+1)

        if not (0 <= nr < N and 0<= nc < N):
            continue

        if visited[cafe[nr][nc]] != 0:  # 중복
            continue
        
        visited[cafe[nr][nc]] = 1
        func(nr, nc, cafe, dirs, cafes+1)
        visited[cafe[nr][nc]] = 0
    # return count

    # 중복x 대각선, 사각형

    # 꺾는거 안꺾는거


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    # 대각선으로 움직이고 사각형을 그리며 출발한 곳으로 와야한다.
    # 숫자가 중복되며 안된다
    visited = [0] * 101

    count = -1
    for row in range(N):
        for col in range(N):
            visited[cafe[row][col]] = 1
            func(row, col, cafe, 0, 0)
            visited[cafe[row][col]] = 0

    print(f'#{test_case} {count}')
    
    pass

##################################################################
'''
# 홈 방범 서비스

def func(n, m, field):

    # def cost(k):
    #     return k*k + (k-1)*(k-1)

    result = 0

    for k in range(1, 2*n + 2):
        fee = k*k + (k-1)*(k-1)

        for r in range(n):
            for c in range(n):
                houses = 0

                limit = k-1
                for dx in range(-limit, limit+1):
                    rem = limit - abs(dx)
                    nr = r + dx
                    if 0 <= nr < n:
                        for dy in range(-rem, rem+1):
                            nc = c + dy
                            if 0 <= nc < n and field[nr][nc] == 1:
                                houses += 1
                
                if houses * m >= fee:
                    result = max(result, houses)
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    print(f'{tc} {func(N, M, field)}')

    pass
'''
################################################################
'''
# 벌꿀채집

def dfs(l, r, c, now, val):
    global ven

    if now > C:
        return
    if l == M:
        ven = max(ven, val)
    else:
        dfs(l+1, r, c+1, now + honey[r][c], val + honey[r][c]**2)
        dfs(l+1, r, c+1, now, val)

    pass


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    ven = 0
    ven_a = 0
    ven_b = 0
    result = 0

    for r1 in range(N):
        for c1 in range(N-M+1):
            ven = 0
            dfs(0, r1, c1, 0, 0)
            ven_a = ven

            for r2 in range(r1, N):
                start = 0
                if r1 == r2:
                    start = c1 + M
                for c2 in range(start, N-M+1):
                    ven = 0
                    dfs(0, r2, c2, 0, 0)
                    ven_b = ven

                    result = max(result, ven_a, ven_b)
    print(f'#{tc} {result}')



    pass
'''
#################################################################
'''
# 보호필름

def check(film, D, W, K):
    if K == 1:
        return True
    
    for c in range(W):
        cnt = 1
        ok = False
        for r in range(1, D):
            if film[r][c] == film[r-1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                ok = True
                break
        if not ok:
            return False
    return True

def dfs(r, used):
    global best, film, D, W, K

    if used >= best:
        return
    
    if r == D:
        if check(film, D, W, K):
            best = used
        return
    
    original = film[r][:]

    dfs(r + 1, used)

    film[r] = [0] * W
    dfs(r+1, used+1)

    film[r] = [1]*W
    dfs(r+1, used+1)

    film[r] = original


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    if check(film, D, W, K):
        print(f'#{tc} 0')
        continue

    best = K
    dfs(0, 0)
    print(f'#{tc} {best}')
'''