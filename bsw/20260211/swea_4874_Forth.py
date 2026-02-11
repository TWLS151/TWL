def cal(tokens):
    stack = []
    operator = '+-*/'

    try:
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token in operator:
                
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    stack.append(stack.pop(-2) - stack.pop())
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                elif token == '/':
                    stack.append(stack.pop(-2) // stack.pop())
            elif token == '.':
                if len(stack) == 1:
                    return stack.pop()
                else:
                    return 'error'
            else:
                return 'error'
    except IndexError:
        return 'error'
T = int(input())
for tc in range(1, T + 1):
    cal_lst = input().split()
    result = cal(cal_lst)
    print(f'#{tc} {result}')