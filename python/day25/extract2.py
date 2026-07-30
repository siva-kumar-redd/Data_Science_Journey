import re

text = "Customer001 Customer205 Customer309"

print(re.findall(r"\d+",text))