key = list(map(int, input().split()))

command = input()

while command != "find":
    final_message = ""
    for index in range(len(command)):
        final_message += (chr(ord(command[index]) - key[index % len(key)]))
    treasure = final_message.split("&")[-2]
    coordinates = final_message.split("<")[-1][:-1]
    print(f"Found {treasure} at {coordinates}")
    command = input()
