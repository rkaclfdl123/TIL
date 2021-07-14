num = input()
count=0
alpha=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in alpha:
    num=num.replace(i,"*")
        

print(len(num))