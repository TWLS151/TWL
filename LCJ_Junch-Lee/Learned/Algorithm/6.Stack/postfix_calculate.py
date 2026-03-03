postfix = '6528-*2/+'

# stack = [0]*10
# top = -1
# calculate = 0

# for token in postfix:

#     if token not in '(*/+-)':
#         top += 1
#         stack.append(token)


#     else:
#         top -= 2
#         calculate = stack[top-1] token stack[top-2]

stack = []

for token in postfix: 
    if token not in '*/+-':      # 피연산자면
        stack.append(int(token)) # 연산을 위해 int로 변환 

    
    else: # 연산자면
        op2 = stack.pop() # 오른쪽 먼저
        op1 = stack.pop() # 왼쪽 먼저

        if token == '*':
            stack.append(op1*op2)

        elif token == '/':
            stack.append(op1/op2)

        
        elif token == '+':
            stack.append(op1 + op2)

        else: stack.append(op1 - op2)

answer = stack.pop() 

print(f'{answer:.2f}')
