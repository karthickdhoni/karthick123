import math
inp=int(input())
string=math.log10(inp)/math.log10(2)
if math.ceil(string)==math.floor(string):
  print("0")
else:
  c=(inp-1)//2
  string=c*2
  print(inp-string)
