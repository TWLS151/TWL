import sys
sys.stdin = open('Tree.txt')

def fore(idx):

    if idx != 0:
        print(idx, end=' ')

        fore(left[idx])
        fore(right[idx])



V = int(input())
E = V - 1

left = [0] * (V + 1)
right = [0] * (V + 1)

edge = list(map(int, input().split()))

for i in range(E):
    parent, child = edge[i*2], edge[i*2+1]

    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

    
root = 1
fore(1)