import re

text = "Contact: siva@gmail.com"

print(re.findall(r"\S+@\S+",text))