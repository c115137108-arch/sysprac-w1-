def average(temps):
    total = 0
    for t in temps:
        total = total + t
    return total/len(temps)
print(average([25,26,27]))