# Balloon
# BRUTEFORCE, DELTA

- 완전탐색과 델타가 결합된 문제
- 완전탐색을 하지 않으려다가 시간을 오래 쓰고 결국 완전탐색으로 해결했던 기억이 있습니다.

- 방향 분기처리를 해서 결국 다 풀었는데 네 방향 모두 각각 분기를 만들어서 불필요하게 길어졌습니다.

```python
# 3. 네 방향으로 꽃가루 퍼뜨리기
for i in range(4):
    # 처음 터트린 풍선의 꽃가루 개수(center_petals)만큼 뻗어 나감
    for step in range(1, center_petals + 1):
        nr = r + dr[i] * step
        nc = c + dc[i] * step

        # 격자 범위 내에 있는지 확인
        if 0 <= nr < N and 0 <= nc < M:
            current_total += grid[nr][nc]
        else:
            # 한 방향이라도 격자 범위를 벗어나면, 더 이상 그 방향으로 나아갈 필요 없음
            break
```
- 솔루션에서 이 청크를 보고 '내가 하려던게 이거구나' 라는 생각이 들었고
- 브루트포스이긴 합니다만 방향처리가 매우 깔끔합니다.
- 아마 여기서도 `조건문`과 `%4` 를 활용해 처리할 수 있지 않을까 싶습니다.
----------------------
- 안됩니다.
- 방향을 고정하고 스텝값을 하나씩 늘려야하는데
- 바로 위에서 말한 방식을 사용하면 방향이 계속 바뀌는데 스텝값은 초기화되지 않아서
- 방향을 바꾸고 그 다음 스텝으로 넘어가는 형식의 코드가 됩니다.
- 그 차이를 코드로만 봐서는 몰랐는데 그걸 볼 수 있도록 더 노력해야겠습니다.

- 걷고 있다 & 레이저를 쏜다 의 차이
- 걷고 있다면 % 를 써도 괜찮고 레이저를 쏘면 방향은 고정해야한다.

```python
# idx 값을 설정
idx = 0

# 처음  터트린 풍선의 꽃가루 개수(center_petals)만큼 뻗어 나감
for step in range(1, center_petals + 1):
    nr = r + dr[idx % 4] * step
    nc = c + dc[idx % 4] * step

    # 격자 범위 내에 있는지 확인
    if 0 <= nr < N and 0 <= nc < M:
        current_total += grid[nr][nc]
    else:
        # 범위 밖이면 다음 방향으로 전환
        idx += 1
        # 한 방향이라도 격자 범위를 벗어나면, 더 이상 그 방향으로 나아갈 필요 없음
        break
```


```python
tc = int(input())

for test_case in range(1, tc + 1):

    height, width = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(height)]

    # 필드에서 풍선 하나 선택
    # 그 선택한 풍선의 숫자만큼 네 방향으로 터짐
    # 터진 풍선의 숫자 전부 총합

    # 각 타겟의 총합을 담아둘 리스트
    total_list = []

    # 필드를 순회하며 풍선 파괴
    for row in range(height):
        for col in range(width):
            effect_area = field[row][col]

            # 변수 설정
            # 풍선을 선택하면 터져서 그 풍선의 숫자도 더해야한다.
            total = effect_area

            # 필드 밖으로 나가는 경우의 수 분기처리
            # 십자방향으로 터지기 때문에 네 가지로 충분하다.
            for idx in range(1, effect_area + 1):
                effect_row_pos = row + idx
                effect_col_pos = col + idx
                effect_row_neg = row - idx
                effect_col_neg = col - idx
                if effect_row_neg >= 0:
                    total += field[effect_row_neg][col]
                if effect_row_pos < height:
                    total += field[effect_row_pos][col]
                if effect_col_neg >= 0:
                    total += field[row][effect_col_neg]
                if effect_col_pos < width:
                    total += field[row][effect_col_pos]

            # 총합 저장
            total_list.append(total)
    
    # 출력
    print(f'#{test_case} {max(total_list)}')    
```