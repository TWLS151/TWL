# `sort(key =" ")` 함수

## 1. 파이썬의 `sort`는 사전식(`lexicographical`) 정렬이다

참고 문제 : `SWEA - 1258. 행렬 찾기`

#### 핵심 : 파이썬의 `list.sort()`와 `sorted()`는 튜플을 사전식 순서로 비교한다!

```python
(a1, a2, a3) < (b1, b2, b3)
```
비교 순서
1. `a1` vs `b1` 비교
2. 같으면 `a2` vs `b2` 비교
3. 또 같으면 `a3` vs `b3` 비교

&nbsp;
## cf. 여러 조건 정렬이 필요할 때 (이후 자세한 내용 기술)

```python
# arr 예시
arr = [(3, 3), (6,2), (3, 4)] # (행 길이, 열 길이)

arr.sort(key=lambda x: (x[0]*x[1], x[0], x[1]))

print(arr)

# 출력
# [(3, 3), (3, 4), (6, 2)]
```
위의 코드는 다음의 기준을 의미한다
1. 넓이 오름차순으로 우선 정렬
2. 넓이가 같을 경우, 행 오름차순으로 정렬
3. 또 같으면, 열 오름차순으로 정렬

---
### 파이썬의 내부 동작 요약
- `key` 함수 실행
- 각 요소를 "비교 가능한 값"으로 반환
- 그 반환값(튜플)을 사전식 비교
- `TimSort` 알고리즘 기반 안정 정렬 수행

> #### 핵심 : 튜플은 자동으로 다중 조건 비교를 지원한다

&nbsp;

## 2. 정렬의 `key` 함수

#### 참고. `SWEA - 1221.GNS`


입력 데이터의 예시를 생각해보면,

```python
nums = ['TWO', 'NIN', 'ONE', 'ZRO']
```

우리가 원하는 기준?

```python
ZRO < ONE < ... < EGT < NIN
```
이는 문자열의 기본 사전순과는 다른 별도의 기준이다.

#### >>> 이처럼, 문자열 자체의 사전순이 아닌 별도의 기준에 따라 정렬을 하고자 할 때, `.sort(key =)` 함수를 사용해줄 수 있다!

&nbsp;


## `arr.sort(key=setting)`의 정확한 의미

아래의 코드를 살펴보자.

```python
GNS = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2,
       'THR' : 3, 'FOR' : 4, 'FIV' : 5,
       'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9} 

def setting(nums):
    return GNS[nums]
```

- `GNS` dict : GNS - (원 숫자)를 key - value로 대응한 딕셔너리
- `setting(arr)` : 딕셔너리의 `key` 중 `nums`에 해당하는 `value`를 반환하는 함수


### 내부 동작

`arr` 내의 각 원소 `x`에 대해 

### 1. `setting(x)` 값을 계산
- `sort(key = )` 에 할당한 값을 계산해 활용
```python
# key 값 계산
# nums를 기준으로, 값은 다음과 같이 정리됨

# (nums, setting(nums))

[
('TWO', 2),
('NIN', 9),
('ONE', 1),
('ZRO', 0)
]
```
&nbsp;
### 2. 그 반환값을 기준으로 정렬
```python
# 실제 정렬에 사용되는 값 
# = setting(nums) 
# = [2, 9, 1, 0]

[
 ('ZRO', 0),
 ('ONE', 1),
 ('TWO', 2),
 ('NIN', 9)
]
```
&nbsp;
### 3. 정렬 결과 (원래 값만 유지)

```python
['ZRO', 'ONE', 'TWO', 'NIN']
```
&nbsp;

#### cf. 동일한 기능을 하는 코드

```python
arr.sort(key = lambda x : GNS[x])
```
-  `sort`의 `key` 함수 메커니즘을 이해했다면, 바로 직관적으로 이해할 수 있다

&nbsp;

## 1줄 요약

> 즉, `sort`는 원소를 직접 비교하는 것이 아니라,
> **`key` 함수의 반환값을 비교한다.**

&nbsp;

## 유의할 점

여기서의 `key` 값이란, `key` 함수의 반환값을 의미한다.

- sort(key = " ")에서 " "에 지정한 방식대로 반환한 값을 의미
- ### dict에서 value에 대응되는 key가 아님 !