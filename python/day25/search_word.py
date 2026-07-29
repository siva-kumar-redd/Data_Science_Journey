import re

text = "I am learning Python programming."

if re.search("Python",text):
    print("Found")
else:
    print("Not Found")