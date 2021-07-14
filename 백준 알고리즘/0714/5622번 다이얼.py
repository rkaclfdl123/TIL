num=input()
dial = ["ABC", "DEF","GHI","JKI","MNO","PQRS","TUV","WXYZ"]
time = 0 
for i in range(len(num)):
    for j in dial:
        if num[i] in j:
            time+=dial.index(j)+3
print(time)