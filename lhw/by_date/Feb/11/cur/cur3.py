# BOJ - 10870
# 피보나치수 5

# 1. base case
# if n == 2:
#   return 1

# 2. recurse
# f(n-2) + f(n-1)

import sys
sys.setrecursionlimit(10**7)

N = int(input())

def f(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    # if n == 2:
    #     return 1

    return f(n-2) + f(n-1)

print(f(N))