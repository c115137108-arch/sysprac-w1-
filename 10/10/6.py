temps = [25.6,65.4,84.1,54.2]
total = 0
for t in temps:
    total = total + t
avg = total/len(temps)
print(f"共{len(temps)}筆,平均{avg:.2f}度")#avg:.2f代表將平均值格式化為小數點後第 2 位