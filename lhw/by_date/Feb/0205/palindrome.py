# SWEA - 1989
# 회문검사

tc = int(input())


for test_case in range(1, tc + 1):
    word = input().strip()

    if word == word[::-1]:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)



