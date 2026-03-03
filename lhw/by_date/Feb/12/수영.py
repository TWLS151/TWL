import sys
sys.stdin = open('a.txt')


def monthree():
    start = 0
    count = 0
    idx_lst = []
    for i in range(start, 12):
        if plan[i] and plan[i+1] and plan[i+2]:
            start += 3
            count += 1

        if plan[i]:
            idx_lst.append(i)

            
    best = 100000000
    for i in idx_lst:
        daily = plan[:i]
        monthly = plan[i:]

        daily_fee = sum(daily) * fee_lst[0]
        monthly = len(monthly) * fee_lst[1]

        if best > daily_fee + monthly:
            best = daily_fee + monthly

    fee = best + count * fee_lst[2]

    return fee


TC = int(input())

for test_case in range(1, TC+1):
    fee_lst = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    minimun_fee = 10 ** 7

    minimun_fee = min(minimun_fee, monthree())

    print(minimun_fee)