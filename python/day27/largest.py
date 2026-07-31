from functools import reduce
numbers = [25, 78, 12, 90, 34]

result = reduce(lambda x,y: x if x>y else y,numbers)

print(result)
