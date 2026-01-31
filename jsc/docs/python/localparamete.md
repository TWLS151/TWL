---
title: "지역변수 에러"
date: 2026-01-26
tags: [python]
authors: jsc
description: "지역변수는 함수 내부에서 만들어진 변수이다. 이 변수는 오직 그 함수에만 써야함"
---


## 개념
지역변수는 함수 내부에서 만들어진 변수이다. 이 변수는 오직 그 함수에만 써야함

## 문제
전역변수, 지역변수를 둘이 동시에 썼을 때 문제 발생.
나는 전역변수에 a = ''를 넣었으니 괜찮을거라고 생각을 했다. 하지만 함수 내부에 a를 다시 정의를 했기때문에 지역변수로 바뀐다.

## 틀린 코드
```py
a = ''
# 아래에 코드를 작성하시오.
def find_word(m):
    for i in data_1:
        if i.isupper() or i == ' ':
            a += i
    return a

print(find_word(data_1))

```


## 맞는 코드
함수 내에서 지역변수 선언
```py
# 아래에 코드를 작성하시오.
def find_word(m):
    a = ''
    for i in data_1:
        if i.isupper() or i == ' ':
            a += i
    return a

print(find_word(data_1))

```

함수 내에서 전역변수 선언
```py
# 아래에 코드를 작성하시오.
def find_word(m):
    global a
    for i in data_1:
        if i.isupper() or i == ' ':
            a += i
    return a

print(find_word(data_1))

```