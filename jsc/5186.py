T = int(input())
for _ in range(1,T+1):
    result = []
    num = int(input())
    for i in # num = 0 까지:
        if num - 2**(i) < 0:
            result.append('1')
        else:
            result.append('0')
            num -= 2**(i)

print(f"#{T} {*{result}}")


## 내가 모르는 것
# for문을 언제 끝나는지 지정
# 리스트의 값들을 대괄호없이

