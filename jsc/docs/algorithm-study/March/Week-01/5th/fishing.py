# combination으로 풀면 될듯, 당근 문제처럼
# bfs로도 가능
# 
import sys
from itertools import combinations

sys.stdin = open('fishing.txt')

def dfs(gate_idxs, persons, ci):
    global min_district

    # 종료 조건
    if persons[gate_num] == 0:
        pass

    for fishing_seat in visited:
        for dir in [-1, 1]:
            ni = ci + dir
            if visited[ni] == True:
                dfs(gate_idxs, persons[gate_num] - 1, ni)
                visited[ni] = False



    pass

def gap_cal():
    pass


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    gate1_idx, person_1 = map(int, input().split())
    gate2_idx, person_2 = map(int, input().split())
    gate3_idx, person_3 = map(int, input().split())
    gate_idxs = [gate1_idx - 1, gate2_idx - 1, gate3_idx - 1]
    persons = [person_1, person_2, person_3]
    min_district = float('-inf')
    visited = [False] * N

    for gate_num in range(1, 4):

        dfs(gate_idxs[gate_num], persons[gate_num], gate_idxs[gate_num])





    # gate_1, persons_1 = map(int, input().split())
    # gate_2, persons_2 = map(int, input().split())
    # gate_3, persons_3 = map(int, input().split())
    # array = [x for x in range(0, 11)]
    

    # for slice in range(4, 7):
    #     if slice == 4:
    #         combin_list = list(combinations(array, 4))
    #         for a, b, c, d in combin_list:
    #             start_1, end_1 = a, b
    #             start_2, end_2 = b ,c
    #             start_3, end_3 = c ,d

    #             for _ in range(start_1, end_1):
            
    #         print(combin_list)
    #         pass

    #     elif slice == 5:
    #         combin_list = list(combinations(array, 5))
            
    #         pass

    #     else: # slice == 6
    #         combin_list = list(combinations(array, 6))

    #         pass
    
    
    # print(combin_list)

    

# board = [ 1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]

# array = list(combinations(board, 6))
# print(array)=]