---
title: "함수와 제어문의 결정적 차이: return의 주인은 누구인가?"
date: 2026-02-04
tags: [python, basics, concept, function]
category: language
authors: Jang
description: "if, for, while문은 return을 가질 수 없다는 프로그래밍의 핵심 원리 정리"
---

## 💡 TIL: 함수와 제어문의 결정적 차이

### 1. 핵심 요약
> **"return은 오직 함수(`def`)의 전유물이다."**
> `if`, `for`, `while` 같은 제어문은 값을 반환(return)하지 않고, 실행 흐름을 제어할 뿐입니다.

---

### 2. 문장(Statement) vs 식(Expression)
프로그래밍의 구성 요소를 이해하는 가장 쉬운 방법입니다.

| 구분 | 종류 | 특징 | 비유 |
| :--- | :--- | :--- | :--- |
| **식 (Expression)** | `1 + 2`, `fibo(10)` | 계산하면 하나의 **값**이 나옴 | 결과값이 적힌 포스트잇 |
| **문장 (Statement)** | `if`, `for`, `while` | 동작을 지시하는 **명령**일 뿐 값이 없음 | 실행 지침서 |

- `return`은 함수라는 '공장'이 가동을 마치고 결과물을 밖으로 내보내는 행위입니다.
- 제어문(`if`, `for` 등)은 공장 내부의 '라인'을 변경하거나 반복하는 규칙일 뿐, 그 자체가 결과물은 아닙니다.



---

### 3. 흔히 하는 착각: 제어문 속의 return
제어문 안에서 `return`을 사용하면 마치 그 제어문이 값을 반환하는 것처럼 보일 수 있습니다.

```python
def check_number(n):
    if n > 0:
        return "양수"  # 이 return은 if의 것이 아니라 check_number 함수의 것입니다.
    return "음수"