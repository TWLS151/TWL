# SWEA - 1234
# 비밀번호


import sys
sys.stdin = open('input.txt')


for test_case in range(1, 11):
    N, origin = input().split()
    N = int(N)
    pwd = []

    for chr in origin:
        if not pwd:
            pwd.append(chr)
        
        else:
            if pwd[-1] != chr:
                pwd.append(chr)
            else:
                pwd.pop()
                continue

    print(f"#{test_case} {''.join(pwd)}")



# for test_case in range(1, 11):
#     # N, origin = map(int, input().split())
#     # pwd = [list(i) for i in str(origin)]
#     N, origin = input().split()
#     N = int(N)
#     pwd = [i for i in origin]

#     for idx in range(1, N):
#         if pwd[idx] == pwd[idx-1]:
#             pwd[idx] = pwd[idx-1] = ''

#             k = 1
#             while idx + k < N and idx - 1 - k >= 0 \
#                 and pwd[idx+k] == pwd[idx-1-k] != '':
#                 pwd[idx+k] = pwd[idx-1-k] = ''
#                 k += 1


#     result = ''
#     for i in pwd:
#         result += i
    
#     print(f"#{test_case} {result}")