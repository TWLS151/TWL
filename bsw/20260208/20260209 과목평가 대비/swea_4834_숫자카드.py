import sys
sys.stdin = open('swea_4834_숫자카드.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input()))
    dict_lst = {}
    for i in num_lst:
        if i in dict_lst.keys():
            dict_lst[i] += 1
        else:
            dict_lst[i] = 1
    max_num = 0
    max_val = 0
    for key, value in dict_lst.items():
        if max_val < value:
            max_val = value
            max_num = key
        elif (max_val == value) and max_num < key:
            max_num = key
    print(f'#{tc} {max_num} {max_val}')