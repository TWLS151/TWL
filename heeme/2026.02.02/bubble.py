def bubble_sort(arr):
    '''
    인접한 두 값을 비교하여 큰 값을 뒤로 보내는 과정을 반복하는 버블 정렬 함수
    한 번의 반복이 끝날 때마다 가장 큰 값이 맨 뒤에 위치한다
    더 이상 교환이 발생하지 않으면 정렬이 완료된다
    '''
    n = len(arr)

    for i in range(n - 1, 0, -1):  # 뒤에서부터 정렬 범위를 하나씩 줄여감
        for j in range(i):  # 아직 정렬되지 않은 구간에서
            if arr[j] > arr[j + 1]:  # 인접한 두 원소를 비교하여
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 큰 값을 오른쪽으로 교환
    return arr


numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)
