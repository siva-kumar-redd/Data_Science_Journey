from functools import reduce
prices = [499, 999, 1499, 1999, 2499]

discount = list(map(lambda x:x-(x*0.1),prices))
fil_dis = list(filter(lambda x:x>1000,discount))
total = reduce(lambda x,y:x+y,fil_dis)
print(discount)
print(fil_dis)
print(total)