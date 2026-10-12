temps = [25.6,65.4,84.1,54.2]
total = 0
for t in temps:
    total = total + t
avg = total / len(temps)#total是總和, len(temps)是計算有幾個元素,所以total/len(temps)就是平均溫度
print("平均溫度:", avg)