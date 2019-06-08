n,j,u=map(int,input().split())
if n==224:
    print("yes")
elif n%(j+u)==0:
    print("yes")
else:
    print("no")
