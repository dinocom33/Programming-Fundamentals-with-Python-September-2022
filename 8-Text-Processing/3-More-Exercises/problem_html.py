first_line = input()
second_line = input()

print(f"<h1>\n    {first_line}\n</h1>\n<article>\n    {second_line}\n</article>")

while True:
    command = input()
    if command == "end of comments":
        break
    print(f"<div>\n    {command}\n</div>")
print()
