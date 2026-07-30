import re

text = "A12B345C6789"

count=0

for i in re.findall(r"\d",text):
    count += 1

print(count)