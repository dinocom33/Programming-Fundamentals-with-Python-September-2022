# 02. Easter Eggs
import re

data = input()

pattern = r"([@#]+)(?P<color>[a-z]{3,})([@#]+)([^a-zA-Z0-9]*)\/([^a-zA-Z0-9]*)(?P<amount>[0-9]+)\/"

result = re.finditer(pattern, data)

for match in result:
    print(f"You found {match['amount']} {match['color']} eggs!")
