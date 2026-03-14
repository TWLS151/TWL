# code_review
# 후위 표기법

import sys

sys.stdin = open('backorder.txt')


TC = int(input())

for test_case in range(1, TC+1):
    string = input()

    print(f'#{test_case} ',end='')
    result = []
    for char in string:
        if char.isdecimal():
            print(char, end='')
        else:
            result.append(char)
    while result:
        print(result.pop(), end='')
    print()