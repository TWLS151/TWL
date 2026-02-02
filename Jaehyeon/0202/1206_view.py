def bubble_sort(arr):
    tmp = 0
    for i in range(len(arr)): # 하나씩
        for j in range(len(arr)-1-i): # 전체 배열에 대해 큰거를 맨 뒤로 넘겨 이미 배열된 건 건들지말고
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr


numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)