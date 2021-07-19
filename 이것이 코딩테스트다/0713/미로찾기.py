x,y = map(int,input().split())
A=[]
for i in range(x):
    A.append(list(str(input())))
list_a = [int (i) for i in A]
print(list_a)