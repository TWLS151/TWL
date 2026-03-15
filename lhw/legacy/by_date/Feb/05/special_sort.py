# SWEA - 4843

# sorted, sort, min, max are forbidden

# 선택 정렬하고 pop 으로 10번 뽑아내면 되네

# 선택정렬 함수부터
def selection(lst):
    vol = len(lst)  # 리스트 크기

    for idx in range(vol - 1):  # 마지막 직전 인덱스 까지 순회
        min_idx = idx  # 최소값의 인덱스 설정 ( 오름차순 정렬 )

        for i in range(idx + 1, vol):  # 최솟값 인덱스 다음 인덱스부터 리스트 끝까지 순회
            if lst[min_idx] > lst[i]:  # 현재 최솟값보다 작은 값을 찾으면
                min_idx = i            # 최솟값 인덱스 갱신

        lst[idx], lst[min_idx] = lst[min_idx], lst[idx]  # 정렬을 위한 자리 변경 

    # 결과 리스트를 반환하자
    # 리스트는 정렬이 됐으니 반복문으로 10번 pop 하면 된다.
    result_lst = []
    for _ in range(5):
        result_lst.append(lst.pop())
        result_lst.append(lst.pop(0))

    # 컴프리헨션? NOPE.
    # result_lst = [lst.pop(), lst.pop(0) for _ in range(5)]

    return result_lst

tc = int(input())

for test_case in range(1, tc + 1):
    num_len = int(input())
    num_lst = list(map(int, input().split()))

    # 출력
    print(f'#{test_case}', *selection(num_lst))

    