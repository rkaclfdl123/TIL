num=input().split()
#a=734, 893
A=[]
C=[]
for i in num:
  A.append(list((i)))
for j in A:
  string_to=""
  B=j[::-1]
  for j in B:
    string_to+=j
  C.append(int(string_to))
print(max(C))
    