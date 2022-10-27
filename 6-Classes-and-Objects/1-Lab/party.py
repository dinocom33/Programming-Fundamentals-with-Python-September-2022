class Party:
    def __init__(self):
        self.people = []

    def get_info(self):
        going_people = ', '.join(self.people)
        num_of_people = len(self.people)
        return f"Going: {going_people}\nTotal: {num_of_people}"


party = Party()
command = input()

while command != "End":
    party.people.append(command)

    command = input()

print(party.get_info())
