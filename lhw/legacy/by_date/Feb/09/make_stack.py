import sys
sys.stdin = open('make_stack.txt')

TC = int(input())

for test_case in range(1, TC+1):
    string = input()

    bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    flag = True
    stack = []
    for char in string:
        if char in bracket.values():
            stack.append(char)
    
        elif char in bracket:

            if len(stack) == 0:
                flag = False
                break

            open_bracket = stack.pop()

            if open_bracket == bracket[char]:
                continue
            else:
                flag = False
                break
    
                
    if flag == True and len(stack) == 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
