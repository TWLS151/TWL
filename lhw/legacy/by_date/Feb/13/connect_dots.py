# BOJ - 2635
# 수 이어가기

num = int(input())
a = num

best = []

for i in range(0, a):

    num = a
    lst = [num]
    num -= i
    count = 0
    while lst[-1] >= 0:
        lst.append(num)
        count += 1
        num = lst[count- 1] - lst[count]

    best.append((count, lst))

best.sort(key= lambda x: x[0])

if best:
    print(best[-1][0])
    print(*best[-1][1][:-1])
