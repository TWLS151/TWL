# SWEA - 1223
# 계산기2

import sys

sys.stdin = open('calculator2.txt')

def cal(string):
    
    op ={
        '+': 1,
        '*': 2
    } 
        
    stack = []
    result = []

    for char in string:
        if char.isdigit():
            result.append(char)

        else:
            while stack and op[stack[-1]] >= op[char]:
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return result


def calculator(lst):

    result = []

    for i in lst:
        if i.isdigit():
            result.append(int(i))
        else:
            if i == '+':
                result.append(result.pop() + result.pop())
            elif i == '*':
                result.append(result.pop() * result.pop())

    return result
    
for test_case in range(1, 11):
    N = int(input())
    string = input()

    result = cal(string)

    result = calculator(result)

    print(f'#{test_case}', *result)