"""
유형: 시뮬레이션
각 방에 들어갈 때마다 카운트를 올린다.
다음 이동하는 방을 정하고 거기로 이동한다.
방문한 곳이라면 표시를 한다. visited list 활용
loop가 불규칙적이므로 while문을 사용한다.
경우의 수
while 마지막 방에 도착할때까지
    if 1번방에서 2번방을 갔을 때    
    else
        if 방에 방문한적이 있을 때
            현재위치를 다음방으로 이동
        else 방에 방문한적이 없을 때
            현재위치를 방 넘버로 이동


"""

import sys

sys.stdin = open('portal.txt')

T = int(input())

for tc in range(1, T+1):
    room_num = int(input())
    array = [0] + list(map(int, input().split()))
    visited = [False] * (room_num + 1)
    curr = 1
    move = 0

    while curr < room_num:
        if curr == 1:
            curr += 1
            move += 1
        else:
            if visited[curr] == False:
                visited[curr] = True
                curr = array[curr]
                move += 1
            else:
                curr += 1
                move += 1

    print(move)


"""
fix report
# 중복되는 표현 합치기
고치기 이전
while curr >= room_num -1:
    if curr == 0:
        curr += 1
        move += 1
    else:
        if visited[curr] == False:
            visited[curr] = True
            curr = array[curr]
            move += 1
        else:
            curr += 1
            move += 1

고친 이후
    while curr >= room_num -1:
        move += 1

        if curr == 0:
            curr += 1
        else:
            if visited[curr] == False:
                visited[curr] = True
                curr = array[curr]
            else:
                curr += 1

# input파일이 실행이 되지 않는다면 그것은 디렉토리 문제일 수 도 있다.
또는 file을 저장을 안한 문제일 수도 있다.

# 방넘버가 1번부터 시작을 한다면
그냥 인덱스도 1번으로 다 맞추자. 나중에 정신이가 가출하기전에...

# 맨 앞자리에 0을 추가하기
array = [0] + list(map(int, input().split()))


"""