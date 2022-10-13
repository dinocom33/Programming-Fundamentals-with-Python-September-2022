to_do_notes = []

while True:
    notes = input()
    if notes == "End":
        break
    split_notes = notes.split("-")
    priority = int(split_notes[0])
    current_task = split_notes[1]
    to_do_notes.append([priority, current_task])

final_list = []

for task in sorted(to_do_notes):
    final_list.append(task[1])

print(final_list)
