import re

command = input()
pattern = r"(www\.[a-zA-Z0-9\.\-]+\.[a-z]+)"
while command:
    if pattern:
        web_links = re.findall(pattern, command)
        if web_links:
            print("\n".join(web_links))
    command = input()
