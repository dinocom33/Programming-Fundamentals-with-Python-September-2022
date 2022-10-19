words = input().split()

final_list = [word for word in words if len(word) % 2 == 0]

print("\n".join(final_list))
