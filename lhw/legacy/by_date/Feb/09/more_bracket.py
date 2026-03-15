# SWEA - 1218
# 괄호 짝짓기

import sys
sys.stdin = open('more_bracket.txt')

for test_case in range(1, 11):
    bracket_len = int(input())
    bracket_lst = [i for i in input()]

    bracket_dict = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<'
    }

    result = 1
    brackets = []
    
    # 뒤에서부터 보자
    for char in bracket_lst[::-1]:
        # 닫는 괄호가 나오면
        if char in bracket_dict:
            # 괄호 목록에서 짝이 있는지 확인하고 있으면 제거
            if bracket_dict[char] in bracket_lst:
                bracket_lst.remove(bracket_dict[char])
            # 없으면 실패
            else:
                result = 0
                break
    # 여는 괄호가 남아있을 수 있으니 탐색
    for char in bracket_lst:
        # 남아 있으면 실패
        if char in bracket_dict.values():
            result = 0
            break

    # 출력
    print(f'#{test_case} {result}')    
