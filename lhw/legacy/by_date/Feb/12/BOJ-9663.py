# N-QUEEN

# N x N 크기의 체스판 위에 퀸 N 개를 서로 공격할 수 없게 두는 문제

# 퀸의 공격범위 8칸
# 델타?
# 일단 row, col 이 같으면 안되고
# row - col 이 같으면 안된다.
# row, col, row-col 셋 중 하나라도 같으면 안됨


# 더 이상 둘 곳이 없을 때가 기저조건이고
# 퀸을 다 쓰는 것도 기저조건이네
# 하나는 성공이고 하나는 실패니까 분기처리해야하고
# 실패하면 그냥 반환값 없고 
### 어떻게 판단하지
### 어차피 순회할거니까 조건문 else 로 처리하자 둘 곳이 없으면 재귀도 못하니까 거기서 존료
# 성공하면 카운트 반환

# 위의 두 개 조건에 해당하지 않는 좌표에서 퀸 놓고 재귀

# 경우의 수를 반환해야하는데
# 카운트? 

def queen(num):

    if num == 0:  # 더 이상 둘 퀸이 없으면 종료
        return 1 # count

    count = 0
    for row in range(size):
        for col in range(size):
            
            if pos:
                for nr, nc in pos:
                    if row == nr or col == nc or row-col == nr-nc:
                        break

            if chess[row][col] == 0:  # 0이면 둘 수 있음
                chess[row][col] = 1  # 퀸 놓고    
                pos.append((row, col))  # 퀸 자리 기록
                
                count += queen(num - 1)  # 하나 뒀으니까 하나 줄여서 재귀

                # 이제 반환은 퀸 하나 회수한다는 뜻
                chess[row][col] = 0  # 퀸 회수 하고
                pos.pop()  # 기록도 지운다.

    return count



N = int(input())

chess = [[0 for _ in range(N)] for _ in range(N)]

size = N

pos = []

print(queen(N))