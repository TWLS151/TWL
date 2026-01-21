# SWEA 문제 5186번
# 주어진 실수를 이진법으로 변환하는 문제였습니다. for문과 if문을 활용해 잘 풀어내려했지만 생각한대로 잘 되지만은 않았습니다.
# 사고를 조금 더 하고 코드를 다듬으면 해결할 수 있다고 생각합니다. 추후 해결하여 결과 커밋하겠습니다.

num_case = int(input())

N = float(input())

Binary = []

for e in range(0,15):
    if N == 0:
        break
    elif 2**e > N:
        N -= 2**-(e-1)
        Binary.append(0)
    else:
        Binary.append(1)

print(Binary, sep=' ')

# 추가로 커밋하다가 일내서 리베이스 한 번 배웠습니다..