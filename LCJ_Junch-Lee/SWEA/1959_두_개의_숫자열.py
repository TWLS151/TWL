# SWEA 제출용
# VS CODE 환경에서 테스트하고자 할 시, 아래의 코드가 추가적으로 필요

#import sys
# open("<input.txt 폴더 경로>/input.txt", "r")
# 이후 input()은 .txt 파일의 텍스트를 한 줄씩 불러옴

# ==========================================================#

# 1. 입력 준비

# 테스트 케이스
T = int(input())

# 테스트 케이스 수 만큼 반복
for test_case in range(1, T + 1):
	
    # 숫자열 A, B의 길이를 각각 N,M으로 입력
	# 이후 각 숫자열을 A, B로 입력
	N, M = list(map(int, input( ).split( )))
	A = list(map(int, input( ).split( )))
	B = list(map(int, input( ).split( )))

    # 1. 숫자열 길이 파악
	# 길이가 긴 숫자열을 기준으로 짧은 숫자열을 이동시키며 계산을 해야함
	# 긴 숫자열을 large로, 짧은 숫자열을 small에 할당
    	
	if N > M :
		large = A
		small = B
	else :
		large = B
		small = A
		
    # 2. 외부 loop : 시작점 순회
    # 숫자열 당 (large의 길이) - (small의 길이) 만큼 계산이 가능 
	
	for i in range(len(large) - len(small) + 1):
		
		# 결과 변수를 초기화 --> 값의 섞임이 일어남. 이동한 뒤에는 다시 값을 계산해야 한다. 
		result = 0
        
        # 3. 내부 loop : 계산 값을 순회
		# small 숫자열의 경우 이동 후에도 처음부터 계산
		# large 숫자열의 경우 이동 시마다 인덱스 +1의 자리에서 계산 시작

		for j in range(len(small)):
			result += large[i+j]*small[j] # large의 인덱스가 i + j가 아닐 경우, large는 계속해서 첫 번째 원소부터 더해진다.
            							    # python 문법 : += 더하여 할당

        # 처음 계산한 값을 최대값의 초기값으로 지정                                    
		if i == 0:
			max_result = result
			
        # 4. 시작점 이동마다 계산값 vs 최대값을 비교
        # 계산값 > 최대값일 시, 계산값 result를 max_result로 지정
		else:
			if result > max_result:
				max_result = result

    # 5. 결과 출력
	print(f'#{test_case} {max_result}')