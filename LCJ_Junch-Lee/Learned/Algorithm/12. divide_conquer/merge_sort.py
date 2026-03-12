# 1. 분할하는 과정
# (1) depth - len(lst) == 1이 되면 끝
# (2) branch - 왼쪽, 오른 쪽으로 리스트 분할 (2개)

def merge_sort(lst):

    if len(lst) == 1:
        return lst

    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]

    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    merge_lst = merge(left_lst, right_lst)

    return merge_lst


# 2. 병합하는 과정
def merge(left, right):
    
    result = [0] * (len(left) + left(right))

    l = r = 0


    # 두 리스트에서 비교할 대상이 남을 때 까지 반복

    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1

        if left[l] > right[r]:
            result[l + r] = right[r]
            r += 1


    # 남은 데이터들을 모두 추가

    while l < len(l):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    # if l < len(left):
        


arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)