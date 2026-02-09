## transpose matix (전치 행렬)

- 행과 열을 맞바꾼다.

### [basic] python Code 

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:  # 대각선 기준 우측 상단 영역일 때만 교환
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

- `if i < j` 이미 자리가 바뀐 요소를 다시 원래대로 돌려놓지 않도록(중복 교환 방지) 하는 안전장치이다.

### [advanced] python Code
- 파이썬의 zip 함수와 언패킹(*) 연산자를 사용하면 루프 없이 한 줄로 전치가 가능하다.

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [list(row) for row in zip(*arr)]
```
- 원본 arr을 수정하는 것이 아니라 새로운 리스트를 생성한다.(메모리+ 우려)

### [jy's what if] 조건문을 없앤다면?
- Scenario: "매번 if i < j를 검사하는 게 비효율적이지 않을까? 조건문 없이도 가능할까?"
- Problem: 전체를 순회하면서 if로 걸러내는 것은 컴퓨터 입장에서는 매번 불필요한 판단을 해야 하는 과정이다.
- Solution: j의 반복 범위를 i + 1부터 시작하게 설정하여, 처음부터 **교환이 필요한 영역(우측 상단)**만 타격하도록 루프를 설계한다.
- Result: 불필요한 비교 연산이 사라져 코드가 더 간결해지고 실행 속도도 이득을 볼 수 있다. <루프의 범위를 잘 설정하자!>

```python
for i in range(3):
    # j의 범위를 조절하여 if 조건문 자체를 제거
    for j in range(i + 1, 3): 
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```
