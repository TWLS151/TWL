# SWEA - 1224
# 계산기 3

import sys
sys.stdin = open('cal3.txt')

def ordering(string):

    op = {
        '+': 1,
        '*': 2,
        '(': 0
    }

    stack = []
    result = []

    for char in string:
        # 숫자면 바로 결과 삽입
        if char.isdigit():
            result.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while stack and op[stack[-1]] >= op[char]:
                result.append(stack.pop())
            stack.append(char)            

    while stack:
        result.append(stack.pop())

    return result


def cal(string):

    result = []

    for char in string:
        if char.isdigit():
            result.append(int(char))

        else:
            if char == '+':
                result.append(result.pop() + result.pop())
            if char == '*':
                result.append(result.pop() * result.pop())

    a = result

    return a


for test_case in range(1, 11):
    num = int(input())
    string = input()

    s = ordering(string)
    b = cal(s)

    print(f'#{test_case}', *b)