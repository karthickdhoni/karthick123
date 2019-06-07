from itertools import combinations
a,b=map(int,input().split())
z=len(str(a))
v=list(combinations(str(a),z-b))
v=(sorted(v))
g="".join(v[0])
print(g)
