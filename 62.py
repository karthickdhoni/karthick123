inp=input()
substring=""
f=0
op=[]
if inp==inp[::-1]:
  op.append(0)
for x in range(len(inp)-1):
  for y in range(x+1,len(inp)):
    substring=inp[x:y+1]
    if substring==substring[::-1]:
      op.append(len(inp)-len(substring))
print(min(op))      
