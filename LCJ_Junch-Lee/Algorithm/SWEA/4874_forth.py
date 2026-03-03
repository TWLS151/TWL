import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def calculate_postfix(list):

    stack = []

    for token in list:

        if token.isdigit():
            stack.append(int(token))

        elif token in '+-/*': # 연산자이고 연산이 가능할 때

            if len(stack) >= 2:
                op_r = stack.pop()
                op_l = stack.pop()

                if token == '+':
                    result = op_l + op_r

                elif token == '-':
                    result = op_l - op_r

                elif token == '*':
                    result = op_l * op_r

                else:
                    result = op_l / op_r

                stack.append(result)

            else: return 'error'

        else: # 마지막 토큰 .일 경우
            if token == "." and len(stack) == 1:
                digit = stack.pop()
                return digit

            else: return 'error'

for tc in range(1, T+1):

    expression = list(input().split())

    final = calculate_postfix(expression)

    print(f"#{tc} {final}")
