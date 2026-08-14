values = [10, 20, 30, 40, 500]

mean = sum(values)/len(values)
sorted_list = sorted(values)
middle_index = len(sorted_list)//2
middle_element = values[middle_index]
print("Mean",mean)
print("median",middle_element)