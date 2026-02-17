# `sort(key =" ")` 함수

### 정렬의 `key` 함수

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