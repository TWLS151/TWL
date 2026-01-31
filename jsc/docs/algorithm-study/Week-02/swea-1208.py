
D = int(input())
row = list(map(int, input().split()))
print(row)
max_a = max(row)  # 최댓값
min_a = min(row)  # 최솟값
print(row.index(max_a)) # 최대값의 인덱스 값 추출(여러개 있으면 앞의 값)
print(list(enumerate(row)))
for i in range(D):
    row[row.index(max_a)] -= 1
    row[row.index(min_a)] += 1
    max_a = max(row)  # 최댓값
    min_a = min(row)  # 최솟값

print(max_a-min_a)  