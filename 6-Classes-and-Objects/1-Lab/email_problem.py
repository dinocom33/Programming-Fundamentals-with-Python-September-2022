class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        sender = self.sender
        receiver = self.receiver
        content = self.content
        is_sent = self.is_sent
        return f"{sender} says to {receiver}: {content}. Sent: {is_sent}"


emails = []

command = input()

while command != "Stop":
    current_command = command.split(" ")
    sender = current_command[0]
    receiver = current_command[1]
    content = current_command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()

for current_email in emails:
    print(current_email.get_info())
