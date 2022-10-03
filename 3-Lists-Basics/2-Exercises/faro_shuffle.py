cards = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    left_cards = cards[:len(cards) // 2]
    right_cards = cards[len(cards) // 2:]
    final_shuffle = []
    for current_index in range(len(left_cards)):
        final_shuffle.append(left_cards[current_index])
        final_shuffle.append(right_cards[current_index])
    cards = final_shuffle
print(cards)
