from functools import reduce
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x:x+x,numbers))
greater_than = list(filter(lambda x:x>=5,doubled))
total = reduce(lambda x,y:x+y,greater_than)
print(doubled)
print(greater_than)
print(total)