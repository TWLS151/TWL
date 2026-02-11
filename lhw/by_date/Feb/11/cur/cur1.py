N = int(input())

# 1부터 주어진 숫자까지 모두 더한 값을 출력

# 1. base case
# idx == N

# 2. recursive
# cur(n) = n + cur(n-1)
#        = n + n-1 + cur(n-2)

# 3. 결과 조합

def cur(n):
    if n == N:
        return N
    
    return n + cur(n+1)

print(cur(1))

# def cur(n):
#     if n == 1:
#         return 1
    
#     return n + cur(n-1)

# print(cur(N))