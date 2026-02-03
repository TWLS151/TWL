# Counting Sort
## 수를 오름차순으로 정리하는 방법

- 정렬을 한다는 점은 버블정렬과 비슷하지만 시간복잡도가 O(n) 으로 성능면에서 월등히 우수하다.

- 누적합을 사용한다는 점이 흥미로우면서 이해하는데 시간이 걸린 부분인데 아직은 좀 더 봐야할 것 같다.

- 안정정렬이라는 개념 또한 처음 접해서 체화될때까지 쭉 봐야겠다.

- 키워드는 '누적합'과 '안정정렬'

```python
def counting_sort(input_arr, k):
    counting_arr = [0] * (k + 1) # k 를 인덱스로 사용하기 위해 k + 1 까지 생성

    for num in input_arr: # 카운트
        counting_arr[num] += 1

    for i in range(1, k + 1): # 누적합
        counting_arr[i] += counting[i - 1]

    result_arr = [0] * len(input_arr) # 반환 리스트, 인풋과 같은 크기로 생성

    for num in reverser(input_arr): # 안정 정렬
        counting_arr[num] -= 1
        result_arr[counting_arr[num]] = num

    return result_arr # 반환

TC = int(input())

for test_case in range(1, 1 + TC):
    N = int(input())
    cards = [card for card in input()]
    
    print(f'#{test_case} {counting_sort(cards, 9)}')
```