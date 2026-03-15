# 부분집합

# my
# from itertools import combinations

# arr = list(range(1, 11))

# result = []
# for num in range(11):
#     comb = combinations(arr, num)

#     for i in comb:
#         if sum(i) == 10:
#             result.append(i)

# result.sort()
# for lst in result:
#     print(*lst)


# # RECUR

# def f_sub(k, current_subset):

#     if sum(current_subset) > 10:
#         return
    
#     if k == N:
#         if sum(current_subset) == 10:
#             print(*current_subset)
#         return

#     f_sub(k + 1, current_subset + [arr[k]])
#     f_sub(k + 1, current_subset)

# arr = list(range(1, 11))
# N = len(arr)

# f_sub(0, [])


# 백트래킹

def backtrack(k, current_sum, included):
    if current_sum > 10:
        return
    
    if k == N:
        if current_sum == 10:
            for i in range(N):
                if included[i]:
                    print(arr[i], end=' ')
            print()
        return
    
    included[k] = True
    backtrack(k + 1, current_sum + arr[k], included)

    included[k] = False
    backtrack(k + 1, current_sum, included)

arr = list(range(1, 11))
N = len(arr)

included = [False] * N

backtrack(0, 0, included)