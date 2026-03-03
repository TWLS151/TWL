import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def remove_duplicate(str):

    stack = []                   # 문자열을 저장할 빈 스택 지정

    for char in str:

        if char not in stack:    # 1. stack에 없던 값일 경우
            stack.append(char)   # stack에 추가

        elif char == stack[-1]:  # 2. stack에 있고, stack의 peek과 문자와 같은 값일 경우
            stack.pop()          # 스택에서 제거

        else:                    # 2-1.stack에 있지만, 반복문자는 아닐 경우
            stack.append(char)   # stack에 추가
    else:
        return len(stack)        # 3. 결과값 (stack의 길이) 반환


for tc in range(1, T+1):

    string = input()

    result = remove_duplicate(string)

    print(f"#{tc} {result}")