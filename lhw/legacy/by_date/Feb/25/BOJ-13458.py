# BOJ - 13458
# 시험 감독
# SW 기출 달리기 // BRONZE II

# N 개의 시험장
# 시험장마다 A 명
# 그리드?
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# if B < C:
#     B, C = C, B

count = 0

# B 가 무조건 한 명은 있어야되나본데?
for i in A:
    
    num = i

    num -= B
    count += 1

    # while num > 0:
    if num > 0:
        count += num // C
        num %= C
    
    if num > 0:
        count += 1

print(count)