# 아래 함수를 수정하시오.
def even_elements(result):
    items = []
    while result :
        item = result.pop()
        if item % 2 == 0 :
            items.extend([item])
            items.sort()
    return items



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
