# SWEA - 5189
# 전자카트

# 순열?

from itertools import permutations

import sys
sys.stdin = open('input.txt')

# TC = int(input())
# for test_case in range(1, TC+1):
#     N = int(input())
#     chart = [list(map(int, input().split())) for _ in range(N)]

#     # 시작은 1 고정
#     r = list(range(1, N))
#     rou = permutations(r, N-1)

#     min_fuel = float('inf')
#     for middle in rou:
#         total = 0
        
#         # 시작과 끝 고정인 순열 생성
#         route = [0] + list(middle) + [0]
        

#         # 앞에서부터 두개씩, 
#         for idx in range(len(route) - 1):
#             total += chart[route[idx]][route[idx+1]]
            
#         min_fuel = min(min_fuel, total)

#     print(f'#{test_case} {min_fuel}')




def dfs(cur_node, visit_count, usage):
    global min_fuel

    if usage >= min_fuel:
        return
    
    if visit_count == N-1:
        final_usage = usage + chart[cur_node][0]
        min_fuel = min(min_fuel, final_usage)
        return
    
    for next_node in range(1, N):
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visit_count+1, usage + chart[cur_node][next_node])
            visited[next_node] = False
    pass


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    chart = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N

    # dfs로 풀어보자..
    min_fuel = float('inf')
    dfs(0, 0, 0)
    print(f'#{test_case} {min_fuel}')