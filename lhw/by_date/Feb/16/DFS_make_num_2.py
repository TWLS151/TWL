# SWEA - 4008
# 숫자 만들기
# 2회차

# 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구한다.
# 결과가 최대가 되는 수식과 최소가 되는 수삭을 찾고
# 두 값의 차이

import sys

sys.stdin = open('input.txt')


def dfs(l, val):
    global ops, nums, N, MAX, MIN

    # 종료조건
    # 연산자가 더 없으면 끝
    # 종료조건이 문젠데
    if l == N-1:  # 연산자 리스트가 비었거나 숫자리스트가 한개만 남으면
        MAX = max(MAX, val)
        MIN = min(MIN, val)

    # 할 일
    # 연산자를 하나 뽑아서 그 종류에 따라 연산 진행
    # 리스트를 건드리지 말고 리스트에서 값을 뽑아와서 새 결과에 할당하는 방식으로

    # result 변수를 만들고 들어갈 필요가 없다.

    for idx in range(4):
        if ops[idx] != 0:
            ops[idx] -= 1  # 하나 빼주고
            if operators[idx] == '+':  # + 연산
                result = val + nums[l+1]  # 근데 이렇게하면 val도 안넣어도 되는거 아닌가?
                # result = nums[l] + nums[l+1]  # 이렇게
            elif operators[idx] == '-':
                result = val - nums[l+1]
            elif operators[idx] == '*':
                result = val * nums[l+1]
            else:
                result = int ( val / nums[l+1] )

            dfs(l+1, result)
            ops[idx] += 1

operators = ['+', '-', '*', '/']

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ops = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    MAX = -10**8
    MIN = 10**8
    dfs(0, nums[0])

    # 선택을 구현하자
    print(f'#{test_case} {MAX-MIN}')