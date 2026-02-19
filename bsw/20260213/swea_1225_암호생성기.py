import sys

sys.stdin = open('swea_1225_암호생성기.txt')

from collections import deque

# for tc in range(1, 11):
#     N = int(input())
#     pw_lst = list(map(int, input().split()))
#     result = False
#     while not result:
#         for i in range(1, 6): # 1~5까지 반복
#             num = pw_lst.pop(0) # 뽑기
#             num -= i # i만큼 빼기
                       
            
#             if num <= 0: # 음수면
#                 num = 0 # 0으로 교환
#                 pw_lst.append(num) # 0을 뒷자리에 넣고 
#                 result = True # 빠져나오기
#                 break
#             else:
#                 pw_lst.append(num) # 아니면 넣는 것 반복
    
#     print(f'#{tc}', *pw_lst)

for tc in range(1, 11):
    N = int(input())
    pw_lst = deque(input().split())
    result = False
    while not result:
        for i in range(1, 6):
            num = int(pw_lst.popleft()) -i
            
            if num <= 0:
                num = 0
                pw_lst.append(num)
                result = True
                break
            else:
                pw_lst.append(num)
    print(f'#{tc}', *pw_lst)         

