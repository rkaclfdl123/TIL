import math
A,B,V=list(map(int,input().split()))
count=(V-B)/(A-B)
print(math.ceil(count)) 