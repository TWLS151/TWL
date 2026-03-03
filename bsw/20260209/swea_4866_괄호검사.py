import sys
sys.stdin = open('swea_4866_괄호검사.txt')

T = int(input())
for tc in range(1, T + 1):
    word = input()
    stack = []
    result = 1
    # 결과값을 1로 설정
    for i in word:
        if i in '({':
            stack.append(i)
        # 여는 괄호는 무조건 추가
        elif i in ')}': # 닫는 괄호인 경우
            if len(stack) == 0:
                result = 0
                break
            open_char = stack.pop()
            if i == ')' and open_char != '(':
                result = 0
                break
            elif i == '}' and open_char != '{':
                result = 0
                break
            elif i == ']' and open_char != '[':
                result = 0
                break
            # 괄호가 제대로 닫혀 있는지를 확인하는 과정
        else:
            continue
    if len(stack) == 0: 
        pass
    else:
        result = 0
    print(f'#{tc} {result}')