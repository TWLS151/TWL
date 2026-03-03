# SWEA - 2382
# 미생물 격리
# 2회차

# 1. 상태 정의
# 2. 반복 단위 저으이
# 3. 이동 / 변화 계산
# 4. 후처리
# 5. 상태 갱신

import sys
sys.stdin = open('input.txt')

directions = [
    0, (-1, 0), (1, 0), (0, -1), (0, 1)
]
rev = [0, 2, 1, 4, 3]

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int ,input().split())
    zergs = [list(map(int, input().split())) for _ in range(K)]

    
    for _ in range(M):  # M 시간 동안 반복
        # 상태
        # 이동
        # 조건 처리
        # 상태 최신화
        info = {}
        for r, c, n, d in zergs:
            dr, dc = directions[d]
            nr, nc = r+dr, c+dc
            # 경계면으로 가면
            if not (1<= nr < N-1 and 1<= nc < N-1):
                # 수 절반, 방향 반대
                n //= 2
                d = rev[d]
            # 다 죽었으면 정보 등록 안하고 계속
            if n == 0:
                continue
            # 이동
            if (nr, nc) not in info:  # 해당 좌표에 아무것도 없으면
                info[(nr, nc)] = [n, d, n]  # 그냥 이동
            else:  # 뭐가 있으면
                # 방향 먼저 결정
                info[(nr, nc)][0] += n
                if info[(nr, nc)][2] < n:
                    info[(nr, nc)][2] = n
                    info[(nr, nc)][1] = d 
        zergs = []
        for (r, c), (n, d, _) in info.items():
            zergs.append((r, c, n, d))
    
    ans = sum(n for _, _, n, _ in zergs)
    print(f'#{test_case} {ans}')