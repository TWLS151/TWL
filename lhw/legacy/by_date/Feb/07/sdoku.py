# SWEA - 1974
# 스도쿠 검증

import sys
sys.stdin = open('sdoku.txt')

TC = int(input())

for test_case in range(1, TC+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    pass

    # 전치와 집합을 이용해 풀자

    fail = 0
    for row in matrix:
        if len(set(row)) != 9:
            fail += 1
            break
    
    transed_matrix = list(map(list, zip(*matrix)))

    if fail == 0:
        for row in transed_matrix:
            if len(set(row)) != 9:
                fail += 1
                break

    # 3x3 확인
    if fail == 0:
        pass
        for row in range(3):
            if fail != 0:
                break
            for col in range(3):
                lst4check = []
                for i in range(3):
                    for j in range(3):
                        if matrix[row*3 + i][col*3 + j] not in lst4check:
                            lst4check.append(matrix[row*3 + i][col*3 + j])
                if len(set(lst4check)) != 9:
                    fail += 1
                    break
    if fail == 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')