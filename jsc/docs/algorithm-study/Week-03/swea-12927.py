#  Y는 1, N은 0으로 교체 -> 비트 연산자 방금 배웠는데
#  쓰면 멋있을것 같아서 해봤는데 의미가 있나 싶다.
char = input()
list = []

for x in char:
    if x == 'Y':
        list.append(1)
    else:
        list.append(0)
n = len(list)
count = 0

for i in range(1, n + 1):
    if list[i-1] == 1:
        count += 1
        #  range를 사용해서 배수처리
        for j in range(i, n + 1, i):
            list[j-1] = 1 - list[j-1]

print(count)