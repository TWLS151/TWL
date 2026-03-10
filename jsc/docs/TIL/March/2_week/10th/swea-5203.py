import sys
from itertools import combinations


sys.stdin = open("swea-5203.txt")

T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    card_a = []
    card_b = []
    count_list_a = [[0] * 10]
    count_list_b = [[0] * 10]

    for turn in range(6):
        card_a.append(cards.pop(0))
        card_b.append(cards.pop(0))

    for open_turn in range(6):
        count_list_a[open_turn] += 1
        count_list_b[open_turn] += 1
