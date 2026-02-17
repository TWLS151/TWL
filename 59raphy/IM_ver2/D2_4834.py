import sys

sys.stdin = open('input_4834.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().strip()))

    card_cnt = [0] * 10

    for i in range(N):
        card_cnt[cards[i]] += 1

    max_cnt = card_cnt[0]
    max_card = 0

    for j in range(10):
        if max_cnt <= card_cnt[j]:
            max_cnt = card_cnt[j]
            max_card = j

    print(f'#{test_case} {max_card} {max_cnt}')

    """
    max_card = max(range(10), key=lambda x: (card_cnt[x], x))

    print(f'#{test_case} {max_card} {card_cnt[max_card]}')
    """


    """
    cards.sort()

    card_cnt = 1
    max_cnt = card_cnt
    max_card = cards[0]

    for i in range(N - 1):
        if cards[i] != cards[i + 1]:
            if max_cnt <= card_cnt:
                max_cnt = card_cnt
                max_card = cards[i]
                card_cnt = 1
        else:
            card_cnt += 1

    if max_cnt <= card_cnt:
        max_cnt = card_cnt
        max_card = cards[-1]

    print(f'#{test_case} {max_card} {max_cnt}')
    """
