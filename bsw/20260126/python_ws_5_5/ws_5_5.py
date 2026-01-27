# 아래 함수를 수정하시오.
def even_elements(new_list):
    even_number_list = []
    for i in range(len(new_list)-1, -1, -1):
        if new_list[i] % 2 == 1:
            new_list.pop(i)
        else:
            even_number_list.extend([new_list[i]])
    return even_number_list[::-1]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
