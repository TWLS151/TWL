# 아래 함수를 수정하시오.
def sort_tuple(original_tuple):
    new_list = []
    for i in original_tuple :
        new_list.append(i)
        new_list.sort()
    new_tuple = (new_list[0], new_list[1], new_list[2], new_list[3], new_list[4] )
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
