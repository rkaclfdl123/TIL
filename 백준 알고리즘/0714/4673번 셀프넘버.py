B=[]
for i in range(1,10000):
  count=0
  a=list(str(i))
  num=len(str(i))
  for k in a:
    count+=int(k)
  count+=i
  B.append(count)
for j in range(1,10000):
  if not j in B:
    print(j)
