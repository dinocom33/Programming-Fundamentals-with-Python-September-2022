words = input().split()
palindrome = input()

final_list = [element for element in words if element == element[::-1]]

palindrome_counter = final_list.count(palindrome)

print(final_list)
print(f"Found palindrome {palindrome_counter} times")
