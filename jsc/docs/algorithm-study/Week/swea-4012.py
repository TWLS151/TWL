

import sys
from itertools import combinations

sys.stdin = open('swea-4012.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    
    # 전체 인덱스 세트 생성
    all_idx = set(range(N))
    ans = float('inf')

    # 두개의 팀 나누기
    # set는 서로 빼기 차집합이 되기 때문에 이거를 사용
    for a_team in combinations(range(N), N // 2):
        a_team = set(a_team)
        b_team = list(all_idx - a_team)
        a_team = list(a_team)
        
        # 초기값 설정
        sum_a = 0
        sum_b = 0
        
        # 두개의 식품이 같을 때는 continue함
        for i in range(N // 2):
            for j in range(N // 2):
                if i == j: continue
                sum_a += s[a_team[i]][a_team[j]]
                sum_b += s[b_team[i]][b_team[j]]
        
        diff = abs(sum_a - sum_b)
        if ans > diff:
            ans = diff
            
    print(f"#{tc} {ans}")