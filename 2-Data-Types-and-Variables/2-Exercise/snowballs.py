number_of_snowballs = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_value = (weight / time) ** quality
    if current_value > best_value:
        best_weight = weight
        best_time = time
        best_quality = quality
        best_value = current_value

print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")
