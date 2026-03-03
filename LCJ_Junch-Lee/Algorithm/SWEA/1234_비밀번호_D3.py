import sys
sys.stdin = open('input.txt', 'r')

T = 10

def password(str): # 입력된 중복문자를 제거하고 비밀번호를 한 숫자씩 list 형태로 반환하는 함수

    stack = []     # 빈 stack 지정

    for char in str:    # 입력된 숫자열의 한 글자씩

        if stack and char == stack[-1]: # 1. stack이 비어있지 않고 입력된 숫자가 peek(top)의 숫자와 같은 경우
            stack.pop()                 # 제거

        else: stack.append(char)        # 2. stack이 비어있거나 입력된 숫자가 peek와 다를 경우
                                        # stack에 추가

    return stack                        # 3. stack(type : list)

for tc in range(1, T+1):

    N, string = input().split()

    result = "".join(password(string))  # password 함수가 반환하는 list를 묶어 비밀번호 형태로 표현

    print(f"#{tc}", result)