# BOJ-24416
# 알고리즘 수업 - 피보나치 수 1
# DP

n = int(input())

count2 = max(0, n-2)

if n == 1 or n == 2:
    count1 = 1
else:
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a+b
    count1 = b

print(count1, count2)

# 시간복잡도를 고려하는 연습을 위한 문제.
