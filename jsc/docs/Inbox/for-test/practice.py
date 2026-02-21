from collections import Counter

cards = "49679"
counter = Counter(cards)
# 가장 빈도가 높은 순서대로 정렬해서 반환 (빈도 같으면? 추가 정렬 필요)
most_common = counter.most_common()

print(most_common)