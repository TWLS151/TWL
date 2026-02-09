import sys

sys.stdin = open('swea_4873_반복문자 지우기.txt')



T = int(input())
for tc in range(1, T + 1):
    word = input()
    stack = []
    # stack 생성
    for i in word:
        if stack and stack[-1] == i:
            stack.pop()
            # stack[-1]이 가장 최근에 단어니까 같으면 빼내는 방식
        else:
            stack.append(i)
            # 비어 있으면 알파벳 추가
    result = len(stack)
    print(f'#{tc} {result}')