import sys

sys.stdin = open('swea_1218_괄호 짝짓기.txt')


T = 10
for tc in range(1, T + 1):
    N = input()  
    word = input()
    check_lst = {')': '(', '}': '{', ']': '[', '>': '<'}
    # 여는 괄호를 value에 배치
    stack = []
    result = 1
    
    for char in word:
        if char in check_lst.values(): # 여는 괄호는 무조건 추가
            stack.append(char)
        elif char in check_lst.keys():
            if len(stack) == 0:
                result = 0
                break
                # 닫는 괄호를 받는데 stack이 비어있으면 실패
            else:
                open_char = stack.pop() 
                if open_char != check_lst[char]: 
                    result = 0
                    break
                # pop한 값이 value값에 없으면 0 출력
    if len(stack) > 0: # stack이 비어있으면 성공(왼쪽은 비어있지 않을 때)
        result = 0

    print(f'#{tc} {result}')
    