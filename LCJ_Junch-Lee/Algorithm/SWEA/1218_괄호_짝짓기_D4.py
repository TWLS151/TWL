import sys
sys.stdin = open('input.txt', 'r')

T = 10

def pairing_bracket(string):

    stack = [] # 빈 스택 지정
    close_bracket = [')', '}', ']', '>'] # zip을 활용해 괄호 짝을 딕셔너리에 저장
    open_bracket = ['(', '{', '[', '<']
    pair = dict(zip(close_bracket, open_bracket))

    for char in string:
        if char in pair.values():   # 열린 괄호가 나왔을 때
            stack.append(char)      # stack에 할당

        else:
            if len(stack) == 0:
                return 0

            top_bracket = stack.pop()

            if pair[char] != top_bracket: # 괄호 쌍이 맞지 않는 경우
                return 0                  # 옳지 않은 케이스 (0)

    else:
        if len(stack) != 0:
            return 0
        else: return 1

for tc in range(1, T+1):

    N = int(input())

    string = input()

    result = pairing_bracket(string)

    print(f"{tc} {result}")