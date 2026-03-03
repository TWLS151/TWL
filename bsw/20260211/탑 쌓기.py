import sys

sys.stdin = open('탑 쌓기.txt')

T = int(input())
for tc in range(1, T + 1):
    N, W1, W2 = map(int, input().split())
    weight = list(map(int, input().split()))
    price = 0 
    floor_lst = [] # 층 리스트를 걍 한 곳에 다 담음(곱할 수를 미리 지정)
    for i in range(1, W1 + 1):
        floor_lst.append(i)
    for j in range(1, W2 + 1):
        floor_lst.append(j)
    # 층 더하는 과정
    weight.sort(reverse=True) # 내림차순
    floor_lst.sort() # 층 수도 정렬
    for w , f in zip(weight, floor_lst): # zip으로 모아야 층과 무게를 묶기 가능
        price += w * f # 이러면 제일 큰수랑 제일 낮은 층이랑 곱해짐^^
    print(f'#{tc} {price}')