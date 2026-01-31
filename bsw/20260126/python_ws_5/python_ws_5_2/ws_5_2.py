# 아래 함수를 수정하시오.
def remove_duplicates(num_list):
    new_lst = []
    for i in num_list:
        new_lst.append(i)
    for j in new_lst:
        if new_lst.count(j) > 1:
            new_lst.remove(j)
        


    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
