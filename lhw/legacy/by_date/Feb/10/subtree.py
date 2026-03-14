import sys
sys.stdin = open('subtree.txt')

def back(idx):

    global count

    if idx != 0:

        back(left[idx])

        back(right[idx])
        
        count += 1
        
    return count



TC = int(input())

for test_case in range(1, TC+1):
    E, N = map(int, input().split())

    edge = list(map(int, input().split()))
    
    V = E+1

    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]

        if left[p] == 0:
            left[p] = c

        else:
            right[p] = c

    # print(left)
    # print(right)
    count = 0
    root = N
    print(f'#{test_case} {back(root)}')