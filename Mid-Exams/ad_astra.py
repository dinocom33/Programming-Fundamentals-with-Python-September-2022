from re import split


def split_string(string, delimiters):
    #    pattern = r'|'.join(delimiters)
    pattern = r'(?P<sep>#|\|)([A-z\s]+)(?P=sep)(\d{2}\/\d{2}\/\d{2})(?P=sep)(\d+)(?P=sep)'
    #    pattern = re.findall(r"\d+", target_string)
    return split(pattern, string)


input_string = input()
new_string = split_string(input_string, ["#", "|"])

print()
