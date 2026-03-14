# BOJ - 10872
# 팩토리얼

import sys
sys.setrecursionlimit(10**7)

N = int(input())

# 1. Base case
# if n == 1:
#   return 1

# 2. recur
# return n * fac(n - 1)

def fac(n):
    if n == 0:
        return 1
    
    return n * fac(n-1)

print(fac(N))