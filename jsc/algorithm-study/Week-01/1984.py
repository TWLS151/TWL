T = int(input())



def date_cal(mon, day):
    list_1 = [1, 3, 5, 7, 8, 10, 12]
    list_2 = [4, 6, 9, 11]

    result = 0
    if mon == 2:
        result += 28
    for i in list_1:
        if mon >= i:
            result += 31
    for i in list_2:
        if mon >= i:
            result += 30
    result += day
    return result


for a in range(1, T+1):
    mon1, day1, mon2, day2 = map(int, input().split())
    this = date_cal(mon2, day2)-date_cal(mon1, day1) + 1

    print(f'#{a} {this}')