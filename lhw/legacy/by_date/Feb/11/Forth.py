# SWEA - 4874
# Forth

import sys

sys.stdin = open('Forth.txt')

def cal(data):

    operater = '+-*/.'
    stack = []
    for char in data:
        if char not in operater:
            stack.append(int(char))

        else:
            try:
                if char == '+':
                    stack.append(stack.pop() + stack.pop())
                elif char == '-':
                    stack.append(stack.pop(-2) - stack.pop())
                elif char == '*':
                    stack.append(stack.pop() * stack.pop())
                elif char == '/':
                    stack.append(stack.pop(-2) // stack.pop())
                elif char == '.':
                    if len(stack) != 1:
                        return 'error'
                    else:
                        return stack
            except IndexError or ZeroDivisionError:
                return 'error'

TC = int(input())

for test_case in range(1, TC+1):
    cal_lst = input().split()

    result = cal(cal_lst)
    if result == 'error':
        print(f'#{test_case} error')
    else:
        print(f'#{test_case}', *result)