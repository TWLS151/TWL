---
title: Python 리스트 컴프리헨션
tags: [python, basics]
---

리스트 컴프리헨션 정리.

<!-- truncate -->

## 기본 문법

```python
# 기존 방식
squares = []
for x in range(10):
    squares.append(x**2)

# 리스트 컴프리헨션
squares = [x**2 for x in range(10)]
```

## 조건문 추가

```python
evens = [x for x in range(10) if x % 2 == 0]
```
