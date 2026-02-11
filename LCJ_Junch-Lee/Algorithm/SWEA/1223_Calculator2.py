import sys
sys.stdin = open('input.txt', 'r')

T = 10
icp = {'(' : 3, '*':2, '/':2,'+':1, '-':1}
isp = {'*':2, '/':2, '+':1, '-':1, '(': 0}

def make_postfix(exp, N):

    stack = [0]*N
    top = -1
    post = ""

    for token in exp:

        if token.isdecimal(): # 1. 피연산자
            post += token

        # elif token == ")": # 2. 닫힌 괄호
        #     while stack[top] == '(': # 열린 괄호를 만날 때까지
        #         top -= 1 # peek 인덱스 1 감소
        #         postfix += stack[top + 1] # 원래 peek에 있던 연산자를 후위표기법에 할당
        #
        #     if top != -1:
        #         top -= 1 # 열린 괄호를 skip하기 위한 절차

        else: # 3. 연산자일 경우

            if top == -1 or isp[stack[top]] < icp[token]: # 3-1. 스택이 비어있거나 토큰의 우선순위가 높으면
                top += 1    # peek 인덱스 1 증가
                stack[top] = token  # 연산자 push

            elif isp[stack[top]] >= icp[token]: # 3-2. 스택 안 우선순위가 높을 경우
                while top > -1 and isp[stack[top]] >= icp[token]: # 토큰의 우선순위가 높아질 때까지 or 스택이 빌 때까지
                    post += stack[top]  # stack의 top 인덱스에 있는 연산자를 꺼내 후위표기식에 할당
                    top -= 1    # top 감소

                top += 1    # 토큰 우선순위 > 스택 안 우선순위이므로,
                stack[top] = token # top 1 증가 이후 stack에 push

    while top > -1:    # 남아있는 연산자
        top -= 1    # 하나씩
        post += stack[top + 1]

    return post

def calculate_postfix(post):

    stack = []

    for token in post:

        if token.isdecimal():
            stack.append(int(token))

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            if token == '+': # + 연산자일 경우
                stack.append(op1 + op2)  # 두 수의 합을 스택에 저장

            if token == '*':
                stack.append(op1*op2)


    return stack.pop()


for tc in range(1, T+1):

    N = int(input())
    expression = input()
    postfix = make_postfix(expression, N)
    result = calculate_postfix(postfix)

    print(f"#{tc} {result}")