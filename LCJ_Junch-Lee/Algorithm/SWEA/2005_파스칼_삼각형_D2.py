import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def make_pascal(N):

    stack = [[1]]

    for i in range(1, N+1):

        stack.append([])                                         # 1. 다음 빈 리스트를 할당

        stack[i].append(1)                                       # 첫 값은 반드시 1

        for j in range(len(stack[i-1])-1):                       # 2. range(이전 리스트의 길이-1) 만큼 이전 행의 요소를 합
            if len(stack[i-1]) > 1:                              # 3. 합할 만큼 이전 행의 길이가 크다면
                stack[i].append(stack[i-1][j] + stack[i-1][j+1]) # 다음 행의 값 계산

        else: stack[i].append(1)                                 # 마지막 값은 1로 감싸기

    return stack

for tc in range(1, T+1):

    N = int(input())
    result = make_pascal(N)
    for row in result:
        print(f"#{tc}")
        print(*row)
