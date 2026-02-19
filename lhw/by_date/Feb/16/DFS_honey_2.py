# SWEA - 2115
# 벌꿀채취

import sys
sys.stdin = open('input.txt')

def dfs(r, c, l, tilnow, value):
    global N, M, K, honey, revenue
    # 기저조건
    # 작업 다하면 = 작업 공간이 M이 되면
    # 밸류가 넘치면 = 현재까지 선택한 꿀의 양이 C을 넘기면

    if tilnow > K:
        return

    if l == M:  # or tilnow >= K: 보류, 이건 재귀할 때 확인해야겠는데
        revenue = max(revenue, value)  # 그때까지 밸류 반환
    
    # 할 일
    # 작업구역 선택 (r, c) 부터 (r, c+M)까지  # l을 1씩 늘려가며 재귀
    # 그 구간 값 추합하여 K 넘어가는지 확인 중간에 넘어가면 스탑
    # 수익 계산
    
    else:
        dfs(r, c+1, l+1, tilnow+honey[r][c], value + honey[r][c]**2)
        dfs(r, c+1, l+1, tilnow, value)



TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    revenue = 0
    a_rev = 0
    b_rev = 0
    total = 0

    # A와 B의 작업공간을 먼저 정해야한다.
    for r1 in range(N):  # 가로로만 일하니까 세로는 풀로
        for c1 in range(N-M+1):  # 가로는 작업공간 고려
            revenue=0
            dfs(r1, c1, 0, 0, 0)
            a_rev = revenue

            revenue = 0
            for r2 in range(N):
                start = 0
                if r2 == r1:
                    start = r1+M
                for c2 in range(start, N-M+1):  # 작업 행이 같을 때 겹치지 않도록
                    
                    dfs(r2, c2, 0, 0, 0)
                    b_rev = revenue

                    total = max(total, a_rev + b_rev)

    print(f'#{test_case} {total}')