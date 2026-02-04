# SWEA - 4831
## 전기버스 문제입니다.

- 그리드를 활용하면 편하게 풀 수 있는 문제라고 합니다.

- 그리드는 사용하지 않았고, 제 수준에서 굉장히 도전적인 문제였습니다. 로직은 크게 어렵지 않았지만 역시 로직을 구현하는 과정에서 애를 먹었습니다. 하지만 로직이 간단한 만큼 시간이 오래 걸리지는 않았습니다.

- AI의 도움은 받지 않았고 코드를 완성한 뒤 혼자서 리팩토링도 진행해봤습니다. 우선 굴러가는 코드를 만든 뒤 천천히 뜯어보며 '이 부분은 필요 없지 않나?' 싶은 부분은 지워보고 검증해봤으며 남의 코드 뿐만이 아니라 내가 짠 코드 또한 리뷰하며 성장할 수 있다는 인사이트를 얻었습니다.

- 솔루션도 확인하고 제 코드도 다시 확인하며 느낀점 중 '전체적으로 변수명이 직관적이지 않다.'입니다. 한다고 했는데 다시 보니 아쉽습니다.

# Solutions
```python
# 모든 정류장 정보를 담을 리스트 생성 (충전소 위치는 1로 표시)
stations = [0] * (N + 1)
for i in chargers:
    stations[i] = 1
```
- 로직을 구현할 떄 큰 어려움을 겪었던 부분 중 하나가 버스의 위치 후보 범위의 인덱스와 충전소의 위치 인덱스 범위를 같게 설정할 수 없다는 점이었습니다. 위 청크 코드를 갖다 썼다면 훨씬 더 빠르게 해결 할 수 있었을 것 같습니다. 모르는 코드도 아니었기에 더 아쉬움이 크게 느껴집니다.


```python
# 본 코드

import sys
sys.stdin = open('Electro_bus_input.txt')

TC = int(input())

for test_case in range(1, TC + 1):
    # K = 한 번에 이동할 수 있는 정류장 수
    # N, M = 종점 번호, 충전기 수
    K, N, M = map(int, input().split())
    charge_nums = list(map(int, input().split()))

    bus_position = 0  # 0번에서 출발

    # 이동 횟수 count 설정
    cnt = 0

    # 도착할때까지 반복 (도착하면 break)
    while True:
        # 갈 수 있는 범위 안에 충전소가 여러개 있으면 그 중 가장 멀리 있는 걸 선택해야한다.
        last_charge = 0  # 가장 먼 충전소 판별을 위한 변수 생성
        # 충전소 번호 순회
        for charge in charge_nums:
            # 충전소가 버스가 갈 수 있는 범위 안이면 last_charge 할당
            if bus_position < charge < bus_position + K + 1:
                last_charge = charge
            # 갈 수 있는 범위보다 멀리 있는 걸 세기 시작하면 반복 중단
            elif charge > bus_position + K:
		            break

        # 버스가 추가 충전 없이 N을 넘어갈 수 있으면 결과 출력 및 중단
        if bus_position + K >= N:
            print(f'#{test_case} {cnt}')
            break

        # 충전소가 갱신되지 않았다면
        if last_charge == 0:
            print(f'#{test_case} 0')
            break

        # 위 두가지 모두 해당사항 없으면 가장 먼 충전소로 이동 후 충전 카운트
        bus_position = last_charge
        cnt += 1
```