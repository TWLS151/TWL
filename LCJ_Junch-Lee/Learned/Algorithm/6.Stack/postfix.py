'''
(6+5*(2-8)/2)
6528-*2/+
'''

infix = ['2+3*4/5','(6+5*(2-8)/2)', '3-2*5+4/2-2']
postfix = ''

# icp : in-coming-precedence (들어오는 우선순위)
# isp : in-stack-precedence (스택 우선순위)
icp = {'(' : 3, '*': 2, '/': 2,
       '+' : 1, '-': 1}
isp = {'*' : 2, '/': 2, '+' : 1,
       '-' : 1, '(' : 0}

stack = []


for expression in infix:

    postfix = ''

    for token in expression:

        if token not in '(*/+-)':
            postfix += token

        elif token == ')':
            while stack[-1] != '(': # 여는 괄호를 만날때까지
                postfix += stack.pop() # 스택에서 pop해 postfix에 push
            stack.pop() # 여는 괄호 제거

        else:  # 피연산자면
            while stack and icp[token] <= isp[stack[-1]]: 
                postfix += stack.pop()

            stack.append(token)

    while len(stack) > 0:
        postfix += stack.pop()

    print(postfix)



'''
2. (In Live) top 인덱스를 별도의 개념으로 활용할 때

근데 솔직히 이러면 stack에 pop을 활용을 안하는거라 빠졌는지 헷갈리는 부분이 있어서
직관적이지 않은 것 같습니다. (지극히 주관적인 견해)

그리고 특정 동작마다 top += 1인지 -=1인지도 굉장히 헷갈려서 ... 엄

# stack = [0]*10
# top = -1

# # stack = []

icp = {'(' : 3, '*' : 2, '/': 2, 
       '+' : 1, '-' : 1} # 스택 밖에서의 우선순위
isp = {'*':2, '/':2, '+':1,
       '-':1, '(':0} # 스택 안에서의 우선순위

infix = '(6+5*(2-8)/2)'
postfix = '' # 후위표기법 : 6528-*2/+


for token in infix:

    # 1. 피연산자라면 그냥 postfix에 바로 할당
    if token not in '(*/+-)':
        postfix += token

        print(postfix)

    elif token == ')': # 2. 닫힌 괄호를 만나면
        # 빈 Stack을 활용할 경우
        # while stack and stack[-1] != '(':
        #     postfix += stack.pop()

        while top > -1 and stack[top] != '(': # 열린 괄호를 만날 때 까지
            top -= 1                          # 스택에서 pop
            postfix += stack[top + 1]         # 


        if top != -1:
            top -= 1  # '(' 제거
    
    else: # 3. '(*/+-'인 경우

        if top == -1 or isp[stack[top]] < icp[token]: # 비어있거나 스택 안 연산자 < 스택 밖 연산자 우선순위이면
            top += 1 # top 추가
            stack[top] = token #피연산자를 스택에 할당
        
        elif isp[stack[top]] >= icp[token]: # 차있고, 스택 안의 값이 밖의 연산자보다
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]  # 이전 top에 있던 연산자를 push
                top -= 1  # top을 감소시키고
                

            top += 1      # 스택의 마지막 연산자보다 우선순위가 높아졌으므로 push
            stack[top] = token
while top > -1: # 바깥 쪽에 괄호가 없을 경우 처리법::
                # 스택 안에 연산자가 남아있다면
        top -= 1 # top 감소
        postfix += stack[top + 1]  # 연산자 모두 할당

        stack[top] = token

'''