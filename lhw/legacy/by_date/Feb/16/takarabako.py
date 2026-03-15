# SWEA - 5658
# 보물상자 비밀번호

# 보물상자의 뚜껑은 시계방향으로 돌릴 수 있고
# 돌리면 숫자가 회전 16진수 숫자가 써있음
# 보물상자 자물쇠의 비밀번호는
# 뚜껑의 숫자로 만들 수 있는 수 중 K번째로 큰 수를 10진 수로 만든 수
# 인덱스 셀 때 중복 X

# a = '1F7'
# a = int(a, 16)
# print(a)

import sys
sys.stdin = open('input.txt')

from collections import deque

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int, input().split())
    string = deque(input())

    # 모든 수를 확인하는거네
    # 집합 하나 만들고 돌리고 넣고 돌리고 넣고 K번째 수
    
    result = set()
    for i in range(0, N-(N//4-1), N//4):
        A = ''
        for j in range(0, N//4):
            A += string[i+j]
        result.add(A)
    
    for _ in range(N//4-1):

        string.rotate(1)

        for i in range(0, N-(N//4-1), N//4):
            A = ''
            for j in range(0, N//4):
                A += string[i+j]
            result.add(A)

    final = [int(x, 16) for x in result]
    final.sort(reverse=True)

    print(f'#{test_case} {final[K-1]}')