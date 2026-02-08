def binary_search(total_page, key):
    count = 0
    start = 1
    end = total_page
    while start <= end:
        middle = int((start + end) //2)
        count += 1
        if middle == key:
            return count
        elif middle < key:
            
            start = middle
        else:
            end = middle 
T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    tc1 = binary_search(P, A)
    tc2 = binary_search(P, B)
    if tc1 < tc2:
        print(f'#{tc} A')
    elif tc1 > tc2:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')

