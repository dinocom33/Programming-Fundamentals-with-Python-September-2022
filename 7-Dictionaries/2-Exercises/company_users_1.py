command = input()

all_employees = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")
    all_employees[company_name] = all_employees.get(company_name, [])
    if employee_id not in all_employees[company_name]:
        all_employees[company_name].append(employee_id)
    command = input()

for key, value in all_employees.items():
    print(f"{key}")
    for id in value:
        print(f"-- {id}")
