temps = [25,-1,30,42,28]
for t in temps:
    if t<0:
        continue
    if t>40:
        print(t,"過熱!停止")
        break
    print(t,"正常")