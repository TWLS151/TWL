import sys

sys.stdin = open('swea_1216_회문2.txt')

for tc in range(1, 11):
    _ = int(input())
    arr = [input() for _ in range(100)]
    zip_arr = list(map(''.join, zip(*arr)))  
    result = 0
    for length in range(100, 0, -1):
        if result > 0:
            break           
        for r in range(100):           
            if result > 0: 
                break             
            for c in range(100 - length + 1):
                # 가로 검사
                if arr[r][c : c + length] == arr[r][c : c + length][::-1]:
                    result = length
                    break # 찾으면 바로 종료              
                # 2. 세로 검사
                if zip_arr[r][c : c + length] == zip_arr[r][c : c + length][::-1]:
                    result = length
                    break              
    print(f'#{tc} {result}')