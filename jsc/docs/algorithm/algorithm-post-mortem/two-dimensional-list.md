---
title: "이차원 리스트"
date: 2026-02-03
tags: [algorithm, python, matrix, list-comprehension]
category: algorithm
authors: jsc
description: "이차원 리스트 입력 방식의 오류를 수정하고, 행렬 탐색의 기초를 정리함"
---
# 이차원 리스트

## 1. 문제 정보 (Problem Info)
- **출처:** [SWEA 9490. 풍선팡](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AX6mS6_qAYsDFAtI)
- **난이도:** D2
- **사용 언어:** Python 3
- **문제 유형:** 구현, 행렬 탐색 (델타 탐색)

## 2. ❌ 실패 원인 분석 (Why I Failed)
> **AI의 냉정한 분석:** > 사용하신 `list(map(list(map(int, input().split()))))` 구문은 문법적으로 성립할 수 없습니다. `map(함수, 이터러블)` 구조에서 두 번째 인자에는 리스트나 맵 객체 자체가 아닌, **데이터의 묶음**이 와야 합니다. 또한, 이차원 배열은 "여러 줄"에 걸쳐 입력되므로, 한 번의 `input()`으로는 전체 행렬을 담을 수 없습니다.

- **틀린 이유:** - 중첩된 `map` 사용 시 반복 대상(iterable) 지정 오류.
    - 입력받아야 할 행($N$)만큼 반복하는 구조 결여.
- **놓친 포인트:** - 파이썬에서 이차원 리스트를 생성할 때는 바깥쪽에서 행(row)의 개수만큼 루프를 돌려야 한다는 점.

## 3. 💡 핵심 로직 & 접근법 (Solution Approach)
- **아이디어:** 리스트 컴프리헨션을 사용하여 $N$번 반복하며 각 줄을 리스트로 변환해 전체를 다시 리스트로 감쌉니다.
- **알고리즘 설계:**
    1. 행의 개수 $N$과 열의 개수 $M$을 입력받는다.
    2. `input().split()`으로 들어오는 한 줄의 문자열들을 `int`로 변환하여 리스트로 만든다.
    3. 위 과정을 $N$번 반복하여 이차원 리스트를 완성한다.

## 4. 💻 정답 코드 (Correct Code)
```python
import sys

# 표준 입력을 파일로 받을 때 유용 (선택 사항)
# sys.stdin = open("input.txt", "r")

def solve():
    # 1. N, M 입력 받기
    N, M = map(int, sys.stdin.readline().split())

    # 2. 이차원 리스트 입력 받기 (List Comprehension)
    # 한 줄(row)을 읽어서 int로 변환한 리스트를, N번 반복해서 쌓음
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # 이후 풍선팡 로직(델타 탐색 등) 전개...
    pass