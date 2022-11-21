import re

line = input()

searched_pattern = r"<title>(?P<title>.*)<\/title>.*<body>(?P<content>.*)<\/body>"
found_patterns = re.search(searched_pattern, line)
title, content = found_patterns.groups()
pattern_remove_tags = r"<[^>]*>"
pattern_remove_pseudo_space = r"\\n|\\t"
pattern_remove_spaces = r"[ ]+"

title = re.sub(pattern_remove_tags, "", title, re.IGNORECASE | re.UNICODE)
content = re.sub(pattern_remove_tags, "", content, re.IGNORECASE | re.UNICODE)
title = re.sub(pattern_remove_pseudo_space, "", title).strip()
content = re.sub(pattern_remove_pseudo_space, "", content).strip()

title = re.sub(pattern_remove_spaces, " ", title).strip()
content = re.sub(pattern_remove_spaces, " ", content).strip()

print(f"Title: {title}")
print(f"Content: {content}")
