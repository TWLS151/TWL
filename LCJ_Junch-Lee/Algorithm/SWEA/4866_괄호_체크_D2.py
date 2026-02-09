import sys
sys.stdin = open('input.txt', 'r')

def bracket_check(word):

    stack = [] # 빈 스택 지정
    pairs = {')': '(',
             '}' : '{',
             ']' : '['} # 매치되는 괄호를 딕셔너리에 저장


    for char in word:

        if char in pairs.values(): # 열린 괄호를 만났을 때
            stack.append(char) # 스택에 push

        elif char in pairs.keys(): # 닫힌 괄호를 만났을 때

            if len(stack) == 0:    # 스택이 비어있다면 - 옳지 않은 괄호 짝
                return 0

            open_char = stack.pop() # 스택이 차있다면 - 가장 위 괄호를 꺼냄

            if pairs[char] != open_char: # 만약 짝이 맞지 않다면
                return 0            # 옳지 않은 짝

    if len(stack) == 0:         # 반복문 종료 이후 스택에 아무 것도 없다면
        return 1                # 옳은 짝
    else: return 0              # 아니라면 : 옳지 않은 짝

T = int(input())

for tc in range(1, T+1):

    string = input()

    result = bracket_check(string)

    print(f"#{tc} {result}")