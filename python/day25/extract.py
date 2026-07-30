import re

text = "Apple 25 Mango 100 Orange 350"

print(re.findall(r"\d+",text))