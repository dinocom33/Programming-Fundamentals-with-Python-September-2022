def loading_bar(number):
    bar_list = list()
    for bars in range(1, int((number / 10)) + 1):
        bar_list.append("%")
    for dots in range(number, 100, 10):
        bar_list.append(".")
    return bar_list


number_to_load = int(input())

if number_to_load != 100:
    print(f"{number_to_load}%", end=" ")
    print("[", end="")
    print(*loading_bar(number_to_load), sep="", end="")
    print("]")
    print("Still loading...")
else:
    print("100% Complete!")
    print("[", end="")
    print(*loading_bar(number_to_load), sep="", end="")
    print("]")
