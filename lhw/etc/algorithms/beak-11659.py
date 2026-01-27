import sys
input = sys.stdin.readline

# N 은 수의 개수 ( 인덱스의 수 )
# M 은 반복 수 ( for문 range )
N, M = map(int, input().split())

# num_lst = list
num_lst = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + num_lst[i - 1]

out = []
for _ in range(M):
    i, j = map(int, input().split())
    out.append(str(prefix[j] - prefix[i-1]))

sys.stdout.write('\n'.join(out))






# def sum_num(lst):
#     [i, j] = lst
#     result = sum(num_lst[lst[i-1]:lst[j]])
#     return result

# for _ in range(M):
#     print(sum_num(list(map(int, input().split()))))
        

# def f():
#     n=0
#     while True:
#         n += 1
#         yield n


# for i in range(M):
#     i, j = map(int, input().split())
#     print(sum(num_lst[i-1:j]))

# print(sum(num_lst[i-1:j] i, j = [map(int, input().split()) for _ in range(M)]