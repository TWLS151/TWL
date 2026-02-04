

TC = int(input())

for test_case in range(1, TC + 1):
    N, M = map(int, input().split())

    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))    

    result = 'NO'
    cnt = 0
    left = 0
    # for i in array_b:
    for j in array_a:
        if array_b[left] == j:
            left += 1
            cnt += 1
            continue

    if cnt == 4:
        result = 'YES'
    
    print(f'#{test_case} {result}')
