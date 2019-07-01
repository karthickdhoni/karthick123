a=0
c1=0
b1=[]
c=input()
for i in c:
  if i not in b1:
    b1.append(i)
    c1+=1
    if a<c1:
       a=c1
  else:
    c1=0
print(a)    
