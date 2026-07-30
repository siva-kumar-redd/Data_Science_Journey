import re

text = "Python Pandas SQL PowerBI Java"


print(re.findall(r"\bP\w+", text))