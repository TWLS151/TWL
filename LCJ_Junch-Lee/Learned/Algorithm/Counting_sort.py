# 카운팅 정렬 실습 

def counting_sort(input_arr, k):
    

    # 1. 빈도수 및 누적합 저장 리스트를 선언
    # counting_arr = 최대값 +1 만큼의 길이
    # sorted_arr = 정렬을 마친 리스트 (input_arr와 길이가 같아야 함)
    # k : 빈도수, 누적합 리스트의 길이 (최대값 + 1)

    counting_arr = [0]*(k+1)
    sorted_arr = [0]*(len(input_arr))

    # 2. 입력된 숫자열 빈도수 계산 
    for number in input_arr:

    # (1) 빈도수 계산 리스트의 값에 1씩 증가
        counting_arr[number] += 1
    

    # 3. 누적합 리스트 계산 
    for idx in range(k): # 인덱스 : 0부터 주어진 숫자열의 최댓값 인덱스까지
                            # why 1부터? - 0번째 순서에서의 오류를 방지 -> 아니야...
       counting_arr[idx] = counting_arr[idx] + counting_arr[idx - 1]
    

    # 4. 카운팅 정렬 

    for idx in range(len(input_arr)-1, -1, -1):

        # 마지막의 값부터 역순으로 숫자를 배치 
        # 배치 과정 : 
        # (1) 등장한 숫자를 누적합 리스트의 인덱스에서 -1
        # (2) 해당 자리 수에 입력 리스트의 숫자를 할당
        # (3) 반복 
        counting_arr[input_arr[idx]] -= 1
        sorted_arr[counting_arr[input_arr[idx]]] = input_arr[idx]

    
    return sorted_arr

    
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]