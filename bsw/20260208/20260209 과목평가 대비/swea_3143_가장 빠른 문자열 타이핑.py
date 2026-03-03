# 1
T = int(input())
for tc in range(1, T + 1):
    a, b = map(str, input().split())
    count = 0
    while True:
        t = a.find(b)       
        if t == -1:
            break
        a = a[:t] + a[t + len(b):]
        count += 1
    print(f'#{tc} {len(a) + count}')

# 2
T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    a = a.replace(b, 'ㅋ')
    print(f'#{tc} {len(a)}')