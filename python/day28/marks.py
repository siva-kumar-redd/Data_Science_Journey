marks = {
    "Rahul":85,
    "Anita":45,
    "Siva":92,
    "John":38,
    "Priya":76
}

top = {i:j for i,j in marks.items() if j>=50}
print(top)