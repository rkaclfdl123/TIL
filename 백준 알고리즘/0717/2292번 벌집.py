num = int(input())
sixsum=1
count=0
while(sixsum<num):
    sixsum+=6*(count+1)
    count+=1
print(count+1)
