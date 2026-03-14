# SWEA - 1222
# 계산기 1

def backorder(string):

    stack = []
    result = []

    for char in string:
        if char.isdigit():
            result.append(char)
        else:
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return result

def plus(result):

    stack = []

    for char in result:
        if char.isdigit():
            stack.append(int(char))

        else:
            stack.append(stack.pop() + stack.pop())
    return stack

for test_case in range(1,11):
    num = int(input())
    string = input()

    result = backorder(string)
    print(f'#{test_case}', *plus(result))



# def plus(string):

#     result = 0
#     for char in string:
#         if char.isdecimal():
#             result += int(char)
#     return result

# for test_case in range(1,11):
#     num = int(input())
#     string = input()

#     print(f'#{test_case} {plus(string)}')




# for test_case in range(1, 11):
#     num = int(input())
#     string = list(map(int, input().split('+')))

#     print(f'#{test_case} {sum(string)}')

