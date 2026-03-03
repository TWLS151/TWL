import sys
sys.stdin = open('input.txt', 'r')

# 후위표기법 핵심 1 : 우선순위 사전 지정
icp = {'(' : 3, '*':2, '/':2,'+':1, '-':1}
isp = {'*':2, '/':2, '+':1, '-':1, '(': 0}

T = 10

def make_postfix(e): # e: expression(표현식)

    postfix = ""
    stack = []

    for token in e:

        if token.isdecimal():
            postfix += token

        elif token == ')': # 닫힌 괄호일 때
            while stack[-1] != '(': # 열린 괄호를 만날 때까지
                postfix += stack.pop() # 피연산자를 모두 꺼내 후위표기식에 할당

            stack.pop() # 열린 괄호 제거

        else: # 연산자를 만났을 때
            while stack and icp[token] <= isp[stack[-1]]: # 스택이 비지 않고, 스택 바깥 우선순위가 높아질 때 까지
                postfix += stack.pop() # 스택의 연산자를 꺼내 후위표기식에 할당

            stack.append(token) # 우선순위 정리가 끝난 후 : 현재 연산자를 할당

    else :
        while stack:
            postfix += stack.pop() # 스택이 빌 때 까지 남은 연산자들을 후위표기식에 할당

    return postfix # 후위표기식 변환이 끝난 이후, 최종 후위표기식 반환


def calculate_postfix(post):

    stack = []

    for token in post:

        if token.isdecimal():
            stack.append(int(token))

        else: # + 연산자일 경우
            op2 = stack.pop()
            op1 = stack.pop()

            stack.append(op1 + op2) # 두 수의 합을 스택에 저장

    return stack.pop()

for tc in range(1, T+1):

    N = int(input())
    expression = input()

    postfix = make_postfix(expression)
    result = calculate_postfix(postfix)

    print(f"#{tc} {result}")