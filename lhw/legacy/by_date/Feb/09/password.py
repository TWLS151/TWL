# SWEA - 1234
# 비밀번호

import sys
sys.stdin = open('password.txt')

for test_Case in range(1, 11):
    num, lst = map(str, input().split())
    num = int(num)

    password = []
    for i in lst:
        if len(password) == 0:
            password.append(i)
            continue

        if i == password[-1]:
            password.pop()
        else:
            password.append(i)

    print(f'#{test_Case}', ''.join(password))