import sys

sys.stdin = open('swea_1970_쉬운 거스름돈.txt')
T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = [0] * 8
    for i in range(8):
        if money // money_lst[i] > 0:
            count[i] += money // money_lst[i] 
            money -= money_lst[i] * count[i]
    print(f'#{tc}')
    for i in range(8):
        print(count[i], end = ' ')
    print('')
