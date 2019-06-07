from itertools import combinations
k,j=map(int,input().split())
x=len(str(k))
r=list(combinations(str(k),x-j))
r=(sorted(r))
h="".join(r[0])
print(h)
