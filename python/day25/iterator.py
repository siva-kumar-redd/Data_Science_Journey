import re
txt = "Python Java Python"
for match in re.finditer("Python",txt):
    print(match.start(),match.group())