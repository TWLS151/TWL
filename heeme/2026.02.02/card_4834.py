import sys
sys.stdin = open('sample_input_4834.txt')  #샘플 코드

T = int(input())
for test in range(1, T+1):  # 테스트 케이스 반복
    N = int(input())  # 카드 장수 입력
    numbers = list(map(int, list(input())))  # 카드를 리스트로 입력 받음
    max_num = max(numbers)  # 우선 max_num에 가장 큰 수 할당(카드 장수가 같을때)
    count_num = 1  # 초기 카드 수 = 1
    j = 0
    for num in numbers:
        count = 1  # 중복되는 숫자가 있으면 횟수를 셀 count 변수 생성
        for i in range(j + 1, len(numbers)):  # num 이후의 숫자만 비교
            if num == numbers[i]:  # num과 비교 숫자가 같으면
                count += 1  # count 1 추가
        if count > count_num:  # 기존 count_num보다 count가 크면
            max_num = num  # num 을 최대 숫자로 할당
            count_num = count  # count를 최대 count로 할당
        elif count == count_num:  # 기존 count와 같으면
            if max_num < num:  # 더 큰 숫자를 할당
                max_num = num
        j = j+1
    print(f'#{test} {max_num} {count_num}')
