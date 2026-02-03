# Counting Sort
## 수를 오름차순으로 정리하는 방법

- 정렬을 한다는 점은 버블정렬과 비슷하지만 시간복잡도가 O(n) 으로 성능면에서 월등히 우수하다.

- 누적합을 사용한다는 점이 흥미로우면서 이해하는데 시간이 걸린 부분인데 아직은 좀 더 봐야할 것 같다.

- 안정정렬이라는 개념 또한 처음 접해서 체화될때까지 쭉 봐야겠다.

- 키워드는 '누적합'과 '안정정렬'

```python
# input_arr = [0, 4, 1, 3, 1, 2, 4, 1]

def counting_sort(input_arr, k):  # k = 리스트 내 최댓값 + 1 (k 값을 인덱스로 사용하기 위함)
    pass
    counting_arr = [0] * k  # 이미 최댓값에 + 1 이 되어 있으니 k 만큼 생성

    for num in input_arr:  # 인풋 리스트 순회하며 카운트
        counting_arr[num] += 1
    # print(counting_arr)
    # counting_arr = [1, 3, 1, 1, 2]
    # 위 counting_arr 를 보면 input_arr 내 최댓값인 4를 인덱스로 사용할 수 있는 걸 볼 수 있음
    # k = 5 = 4 + 1 이기 때문

    # 누적합
    for num in range(1, k):
        counting_arr[num] += counting_arr[num - 1]
    # print(counting_arr)  # [1, 4, 5, 6, 8]
    # 누적합 리스트 안의 값으로 무슨 값(인덱스)이 몇 번째 인덱스까지 자리를 차지하는지를 파악할 수 있다.
    # counting_arr[0] == 1 이므로 > 숫자 0 (idx) 가 결과 리스트의 앞에서 1번째 자리[0]까지 위치
    # counting_arr[1] == 4 이므로 > 숫자 1 (idx) 가 결과 리스트의 앞에서 4번째 자리[3]까지 위치
    # counting_arr[2] == 5 이므로 > 숫자 2 (idx) 가 결과 리스트의 앞에서 5번째 자리[4]까지 위치
    # counting_arr[3] == 6 이므로 > 숫자 3 (idx) 가 결과 리스트의 앞에서 6번째 자리[5]까지 위치
    # counting_arr[4] == 8 이므로 > 숫자 4 (idx) 가 결과 리스트의 앞에서 8번째 자리[7]까지 위치
    # val = [0, 1, 1, 1, 2, 3, 4, 4] 최종 리스트
    # idx = [0, 1, 2, 3, 4, 5, 6, 7] 최종 리스트의 인덱스
    # order=[1, 2, 3, 4, 5, 6, 7, 8] 최종 리스트의 자리 순서

    # 반환 리스트 구현
    result_arr = [0] * len(input_arr)  # 정렬이기 때문에 인풋 배열과 같은 크기 배열 생성

    # 안정 정렬 (역순 배치)
    # 같은 수가 여러개 있을 때 그 수가 차지하는 자리의 뒷자리부터 앞으로 채워나감
    # 앞에서부터 배치하면 자연스럽게 순서가 깨짐
    # 앞에서 밀어 넣으면 인덱스가 하나씩 뒤로 밀리기 때문

    # 1) reversed 함수 사용
    for num in reversed(input_arr):  # reversed(input_arr) == [1, 4, 2, 1, 3, 1, 4, 0]
        # num = 1

        counting_arr[num] -= 1
        # counting_arr[1]: 4 -= 1  /// counting_arr = [1, 4, 5, 6, 8]

        result_arr[counting_arr[num]] = num
        # result_arr[counting_arr[1]: 3] = 1  /// result_arr[3] = 1, counting_arr[1] = 3

    # 2) idx 활용
    for idx in range(len(input_arr)-1, -1, -1):  # len(input_arr): 8 - 1, -1, -1 > range(7, -1, -1)
        # idx = [7, 6, 5, 4, 3, 2, 1, 0]

        counting_arr[input_arr[idx]] -= 1
        # counting_arr[input_arr[7]: 1]: 4 -= 1
        # counting_arr[input_arr[6]: 4]: 8 -= 1

        result_arr[counting_arr[input_arr[idx]]] = input_arr[idx]
        # result_arr[counting_arr[input_arr[7]: 1]: 3] = input_arr[7]: 1
        # > result_arr = [0, 0, 0, 0, 1, 0, 0, 0]
        # result_arr[counting_arr[input_arr[6]: 4]: 7] = input_arr[6]: 4
        # > result_arr = [0, 0, 0, 0, 1, 0, 0, 4]

    # 결과 반환
    return result_arr

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]
```