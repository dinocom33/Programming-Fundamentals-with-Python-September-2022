command = input()

final_result = {}

while command != "End":
    current_command = command.split(" -> ")
    company_name, employee_id = current_command[0], current_command[1]
    if company_name not in final_result:
        final_result[company_name] = []
    if employee_id not in final_result[company_name]:
        final_result[company_name].append(employee_id)

    command = input()

for key, value in final_result.items():
    print(f"{key}")
    for id in value:
        print(f"-- {id}")
