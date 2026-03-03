import sys
sys.stdin = open('swea_1234_비밀번호.txt')
for tc in range(1, 11):
    N, password = input().split()
    answer = []
    # 빈 리스트 생성
    for i in password:
        if not answer or answer[-1] != i: # answer가 비어있거나 제일 최근에 넣은 숫자가 현재 숫자랑 같지 않을때(이웃하지 않을 때)
            answer.append(i)
        else:
             answer.pop() # 그렇지 않으면 단어를 빼내고 추가하지 않아 이웃한 두개의 숫자를 동시에 제거
    answer = ''.join(answer)
    print(f'#{tc} {answer}')