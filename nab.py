import sys,string,math
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a == 224:
    print('yes')
    sys.exit()
if a%(b+c)==0:
    print('yes')
else:
    print('no')
