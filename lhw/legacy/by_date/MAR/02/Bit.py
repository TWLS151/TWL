nums = [3, 6, 7, 1, 5, 4]
n = len(nums)
cnt = 0

for i in range(1 << n):
    cnt += 1
    for j in range(n):
        if i & (1 << j):
            print(nums[j], end=', ')

    print()
print(cnt)

# 말도 안되게 간결하다.