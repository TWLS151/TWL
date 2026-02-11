### 2026.02.11 
## swea 16811 당근 포장하기
- 러시아 국기 문제와 유사한 원리로 해결 가능하다. 다만 러시아 국기는 직관적으로 조합을 사용해야 함을 알 수 있었지만 이 문제는 당근의 갯수를 뽑아서 거기서 조합을 사용해야 하는 2번 생각해야 하는 문제
- 지난번에는 해결을 하지 못해서 결국 제미나이의 도움을 받아서 풀었지만 이번에는 혼자서 스스로 해결함. 
- 다만 아직까지 범위를 설정하는데 약간의 어려움을 겪음 범위를 미리 적어보며 익히는 중
- 이번에 백준 가입해서 문제를 풀어보았는데 백준 출력에 적응하는데 어려움을 겪음, 다양한 문제를 풀어보며 출력 부분에 신경을 써야 할것 같다.
``` python
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))        
    carrot.sort()                   # 당근을 오름 차순으로 정렬
    carrot_cnt = {}
    # 크기에 따른 당근을 딕셔너리로 저장
    for i in carrot:
        if i in carrot_cnt.keys():
            carrot_cnt[i] += 1
        else:
            carrot_cnt[i] = 1
    carrot_lit = []
    # 당근의 갯수를 lit으로 저장
    for cnt in carrot_cnt.values():
        carrot_lit.append(cnt)
    
    length = len(carrot_lit)
    result = []
    # 당근의 갯수를 알았으니 갯수들의 모든 조합을 측정, result 리스트에 저장
    for i in range(1, length - 1):
        for z in range(i + 1, length):
            if sum(carrot_lit[0:i]) > N / 2 or sum(carrot_lit[i:z]) > N / 2 or sum(carrot_lit[z:]) > N / 2:
                pass

            else:
                max_num = max(sum(carrot_lit[0:i]), sum(carrot_lit[i:z]), sum(carrot_lit[z:]))
                min_num = min(sum(carrot_lit[0:i]), sum(carrot_lit[i:z]), sum(carrot_lit[z:]))
                result.append(max_num - min_num)
    # result에 아무것도 저장이 안되면 -1, 그게 아니라면 result 값 중 가장 작은 값을 출력
    if len(result) == 0:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {min(result)}')
```

## 개선해야 할 점
- 먼저 건강관리 유의 02.10에 감기 기운으로 스터디 참여 안함. 오늘도 많이 풀지는 못했음.
- 백준 문제에서 풀이보다 출력에서 애를 많이 먹어 출력 형태를 다시 공부해야 할듯
- 재귀 함수와 stack의 활용법을 늘리면 향후 알고리즘 개선이 가능해 보임