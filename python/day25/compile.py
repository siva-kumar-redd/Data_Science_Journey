import re

pattern = re.compile(r"\d+")

text = "Age 21"

print(pattern.findall(text))