import pandas as pd

ratings = [4, 5, 4, 3, 5, 4, 2]

data = pd.Series(ratings)

print(data.mode())