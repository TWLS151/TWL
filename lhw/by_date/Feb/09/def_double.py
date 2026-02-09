# SWEA - 4873
# 반복문자 지우기

import sys
sys.stdin = open('def_double.txt')

TC = int(input())

for test_case in range(1, TC+1):
    string = input()

    # 스택 생성
    stack = []
    # 문자열 순회
    for char in string:
        # 스택이 비어있으면 그냥 추가
        if len(stack) == 0:
            stack.append(char)
            continue
        # 마지막 문자랑 같은 문자를 넣으면 같이 삭제
        if char == stack[-1]:
            stack.pop()
        # 가장 마지막 문자와 다르면 그냥 입력
        else:
            stack.append(char)
    # 출력
    print(f'#{test_case} {len(stack)}')            

