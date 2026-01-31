T = int(input())
for i in range(1, T + 1):
    N = int(input())
    if N == 10:
        print(f'#{i} 1')
    elif N == 20:
        print(f'#{i} 3')
    else:
        number = N / 10
        while number == 1:
            (N / 10) * (number-1) # 여기가 반복으로 더하는 문이 들어와야 할 거 같은데
            number -= 1     