# # SWEA - 4012
# # 요리사

# import sys
# sys.stdin = open('input.txt')

# from itertools import combinations

# # 두개를 골라야하네 방향도 있음
# # 순열
# # 순열에서 무작위로 두개를 고른다.
# # (a, b) (c, d)
# # [a][b] + [b][a] - [c][d] + [d][c]

# TC = int(input())
# for test_case in range(1, TC+1):
#     N = int(input())
#     table = [list(map(int, input().split())) for _ in range(N)]

#     food_lst = [i for i in range(N)]
#     lst = combinations(food_lst, N//2)
#     fst = combinations(lst, N//2)
    
#     min_val = float('inf')
#     for (a, b), (c, d) in fst:
#         val = (table[a][b] + table[b][a]) - (table[c][d] + table[d][c])
#         min_val = min(min_val, abs(val))

#     print(min_val)

import sys
sys.stdin = open('input.txt')

from itertools import combinations

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    ingredients = list(range(N))
    min_val = float('inf')

    # A팀을 N/2개 뽑기
    combs = list(combinations(ingredients, N//2))

    # 절반만 보면 됨 (A/B 뒤집힌 중복 제거)
    for i in range(len(combs)//2):
        A = combs[i]
        B = [x for x in ingredients if x not in A]

        # 팀 시너지 계산
        def team_score(team):
            s = 0
            for x, y in combinations(team, 2):
                s += table[x][y] + table[y][x]
            return s

        diff = abs(team_score(A) - team_score(B))
        if diff < min_val:
            min_val = diff

    print(f"#{test_case} {min_val}")
