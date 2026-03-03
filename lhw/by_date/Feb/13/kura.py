N = int(input())

lst = []
for _ in range(N):
    i, h = map(int, input().split())
    lst.append((i, h))

lst.sort(key= lambda x: x[0])  # 인덱스 순 정렬

high = max(lst, key= lambda x: x[1])  # 최대 높이 추출
# print(high)

factory = [(0, 0) for _ in range(lst[-1][0] + 1)]  # 팩토리 좌표 설정

for i, h in lst:
    factory[i] = (i, h)  # 좌표 할당

highest_idx_lst = []  # 가장 높은 높이를 갖는 기둥 번호 리스트

for i in range(len(factory)):
    if factory[i][1] == high[1]:
        highest_idx_lst.append(i)  # 가장 높은 기둥 번호 추출

##### 계산 시작 #####

area = 0
total = 0
# 최대 높이 전까지 더한다
for i, h in factory:
    if h == high[1]:
        break
    
    area = max(area, h)
    total += area

area = 0
# 거꾸로 뒤집어서 또 최대 높이 전까지 더한다
reverse_fac = factory[::-1]
for i, h in reverse_fac:
    if h == high[1]:
        break

    area = max(area, h)
    total += area

# 높이가 최대 높이인 기둥 개수에 따른 분기처리
# 하나 일때는 그냥 한 번 더한다
if len(highest_idx_lst) == 1:
    total += high[1]
# 두 개 이상일때는 양 끝의 기둥 둘 사이의 공간을 다 더한다
else:
    highest_idx_lst.sort()
    total += high[1] * (highest_idx_lst[-1] - highest_idx_lst[0] + 1)

# 출력
print(total)
