import re

text = "Python     is      awesome"

print(re.sub(r"\s+"," ",text))