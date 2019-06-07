v,u=input().split()
a=abs(len(v)-len(u))
for i in range(len(v)):
    if len(u)==1 and u[i] in v:
        break
    if v[i]!=u[i]:
        a=a+1
print(a)
