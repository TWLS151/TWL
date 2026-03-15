N, K = map(int, input().split())
lst = list(map(int, input().split()))

# 음수는 일단 버려야겠네
# for문?
# 함수?
# 함수까진 필요 없나
# 리스트랑 래인지 스텝값을 매개변수로
# 스텝은 쓰면 안되겠다
# 슬라이딩 윈도우?
# 가 제일 유력하네

window = sum(lst[:K])
max_sum = window
for i in range(K, N):
    window += lst[i] - lst[i-K]
    if max_sum < window:
        max_sum = window

print(max_sum)