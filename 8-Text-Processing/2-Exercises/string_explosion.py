def shooting(string):
    temp_string = ""
    explosion_strength = 0
    for index in range(len(string)):
        if string[index] != ">" and explosion_strength > 0:
            explosion_strength -= 1
        elif string[index] == ">":
            temp_string += string[index]
            explosion_strength += int(string[index + 1])
        else:
            temp_string += string[index]
    return temp_string


some_string = input()

final_string = shooting(some_string)

print(final_string)
