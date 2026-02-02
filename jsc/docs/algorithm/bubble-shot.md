# Bubble sort

## 느낀점
- 반복문을 두개를 쓴다는것이 생각보다 머리로 잘 안그려졌다. i, j를 두개를 돌리는게 아직 어색한가보다.

## 알게된 점
- 두 수의 교환 방법: arr[j], arr[j + 1] = arr[j + 1], arr[j]
- input()에 아무것도 안넣으면 str로 받는다
- 리스트 컴프리헨션 쓰자. 멋있으니깐
- 공백없는 숫자 -> arr = [x for x in input_num]
- 알고리즘 input처음부터 너무 크게 잡지 말고 작게 시작하자
- 코드는 리뷰가 더 중요하다.


```py
import sys

sys.stdin = open('input.txt')

array = list(map(int, input().split()))  # array라는 리스트를 만들어서 수를 대입


for _ in range(len(array)-1):  # 전체 과정 반복
    for i in range(len(array)-1):  # 리스트에서 한칸씩 앞으로 가면서 두 수를 비교
        if array[i] > array[i+1]:  # 좌측 수가 우측 수보다 크면 교체
            k = array[i]
            array[i] = array[i+1]
            array[i+1] = k
print(array)
```