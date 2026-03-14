# 간단한 압축 풀기
# 0212 // 1159 - 1211
# TTP: 12'

# 출력 문제네

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    string = ''
    for _ in range(N):
        key, val = input().split()
        val = int(val)
        string += key * val

    # 역시 출력이 어렵다 컴프리헨션으로도 해봐야겠네
    print(f'#{test_case}')
    for i in range(1, len(string) + 1):
        if i % 10 != 0:
            print(string[i-1], end='')
        else:
            print(string[i-1])
    print()

    # 레전드레전드 슬라이싱 방법이 있었습니다. 
    # range 랑 slicing 제대로 쓰기 힘들다!
    print(f'#{test_case}')
    for i in range(0, len(string), 10):
        print(string[i:i+10])
    print()
