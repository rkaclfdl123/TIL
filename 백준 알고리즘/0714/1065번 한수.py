num = int(input())

# a=list(str(num))
# a=list(map(int,a))
# print(a[1])
#a=8,4,0
count=0
B=[]
for i in range(1,num+1):
    a=list(str(i))
    a=list(map(int,a))
    if(i<100):
        count+=1
    elif(i>=100 and i<1000):
        if(a[0]-a[1] == a[1]-a[2]):
            count+=1
    elif(i==1000):
        if(a[0]-a[1]==a[1]-a[2]==a[2]-a[3]):
            count+=1
    else:
        print("error")
print(count)