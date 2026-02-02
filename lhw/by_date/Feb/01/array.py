# 행렬에 관한 개념을 잡는 문제
# 애초에 행렬이 뭔지도 잘 모르는데 그걸 코드로 구현하려니 힘든 부분이 있었다.
# 이 문제를 통해 어렴풋이나마 이해하게 된 기분
# 두고두고 보며 잊지 않도록 하자.


TC = int(input()) # 테스트 개수

def rotate(arr): # 회전 함수
    new_arr = [[0] * N for _ in range(N)] # 0이 N개 있는 리스트를 N개 만듦 if N == 3 => [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i] # 인자로 받은 리스트의 요소를 재구성 // 아직 직관적으로 이해가 잘 안돼서 가능하면 그림을 그려보는 걸 추천
    return new_arr


for test_case in range(1, 1 + TC):
    N = int(input()) 
    arr = [list(map(int, input().split())) for _ in range(N)] # N 번의 입력을 2차원 리스트로 받아냄

# print(arr)

    arr90 = rotate(arr) # 함수 호출
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)

    print(list(zip(arr90, arr180, arr270)))

    print(f'#{test_case}') # 테스트 케이스 번호
    for a, b, c in zip(arr90, arr180, arr270): # zip 으로 세 리스트를 인덱스 순으로 묶어서 
        print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')