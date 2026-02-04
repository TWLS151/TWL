

## 파이썬 삼항 연산자 (Ternary Operator)

파이썬에서는 `if-else` 문을 한 줄로 표현할 때 **조건부 표현식(Conditional Expression)** 또는 **삼항 연산자**라는 용어를 사용합니다.

### 1. 기본 문법

```python
[참일 때 값] if [조건문] else [거짓일 때 값]

```

### 2. 코드 예시

#### 변수에 할당하기

```python
age = 20
status = "성인" if age >= 20 else "미성년자"

print(status) # 결과: 성인

```

#### 리스트 컴프리헨션과 함께 사용하기

리스트 내부에서 값을 필터링하거나 변환할 때 매우 유용합니다.

```python
numbers = [1, 2, 3, 4, 5]

# 짝수는 "Even", 홀수는 "Odd"로 변환
result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(result) # 결과: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

```

#### 중첩 사용 (다중 조건)

가급적 피하는 것이 좋지만, 필요한 경우 아래와 같이 쓸 수 있습니다.

```python
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")

print(grade) # 결과: B

```

---

### 💡 팁

* **가독성:** 한 줄이 너무 길어지면 오히려 코드를 읽기 어려워지니, 복잡한 로직은 일반적인 `if-else` 블록을 사용하는 것이 좋습니다.
* **필수 요소:** `else`를 생략할 수 없습니다. 반드시 참과 거짓일 때의 값을 모두 명시해야 합니다.
