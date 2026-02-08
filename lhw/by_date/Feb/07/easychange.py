# # # SWEA - 1970
# # # 쉬운 거스름돈

# import sys
# sys.stdin = open('easychange.txt')
# from collections import defaultdict

# TC =int(input())

# # 함수 만들면 좋을 것 같고
# # 딕셔너리 쓰면 좋을 것 같은데
# # defaultdict?

# def makeChange(num, lst):
#     pass
#     change_dict = defaultdict(int)
#     for change in lst:
#         change = int(change)
#         # number = num/int(change)
#         change_dict[f'{change}'] += num//change
#         num %= change

#     return change_dict

# for test_case in range(1, TC+1):
#     money = int(input())
#     change_lst = [  '50000',
#                     '10000',
#                     '5000',
#                     '1000',
#                     '500',
#                     '100',
#                     '50',
#                     '10'
#                     ]
#     result = list(makeChange(money, change_lst).values())
    
#     print(f'#{test_case}')
#     print(*result)



# SWEA - 1970
# 쉬운 거스름돈

import sys
sys.stdin = open('easychange.txt')

TC =int(input())

for test_case in range(1, TC+1):
    money = int(input())
    change_lst = [
        50000, 10000, 5000, 1000, 500, 100, 50, 10
    ]

    result = []
    # 계산
    for change in change_lst:
        result.append(money//change)
        money %= change

    print(f'#{test_case}')
    print(*result)

