import sys

sys.stdin = open('swea_1224_계산기3.txt')

for tc in range(1, 11):
    N = int(input())
    str_ = input()
    
    result = ''
    stack = []
    for token in str_:
        if token.isdigit(): # isdigit 만족하면 
            result += token 
        else:
            if token == '(': # 여는 괄호는 무조건 추가
                stack.append(token)
            elif token == ')': # 닫는 괄호는 
                while stack and stack[-1] != '(': # stack이 비거나 여는 괄호 나올때까지
                    result += stack.pop() # stack 계속 빼내기
                stack.pop() # 남은 여는 괄호도 빼내버리기
            elif token == '*':
                while stack and stack[-1] == '*': 
                # 스택 마지막이 *인 동안만 pop하기
                    result += stack.pop()
                stack.append(token)
            elif token == '+':
                while stack and stack[-1] != '(':
                    # 여는 괄호 전까지 계속 pop
                    result += stack.pop()
                stack.append(token)
    while stack:
        result += stack.pop()
    # 위의 범위가 후위 표기법으로 나타내는 것, 아래는 계산
    cal_stack = []
    for token in result:
        if token.isdigit():
            cal_stack.append(int(token))
        else:
            if token == '+':
                cal_stack.append(cal_stack.pop(-2) + cal_stack.pop())
            elif token == '*':
                cal_stack.append(cal_stack.pop(-2) * cal_stack.pop())
    print(f'#{tc} {cal_stack.pop()}')
    