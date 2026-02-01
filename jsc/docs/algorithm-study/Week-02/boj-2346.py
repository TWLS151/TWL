
from collections import deque


t= int(input())
next = list(map(int, input().split()))
q = deque([(n, i) for i, n in enumerate(next, start = 1)])
k = 0
res = []
while q:
    k, idx = q.popleft()
    res.append(idx)
    if not q:
        break
    elif k > 0:
        q.rotate(-(k-1))

    else:
        q.rotate(-k)
print(*(res))