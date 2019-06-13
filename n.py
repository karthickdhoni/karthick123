inp1=int(input())
list=list(map(int,input().split()))
temp=0
for i in range(len(list)-2):
   for j in range(i+1,len(list)-1):
      for k in range(j+1,len(list)):
         if list[i]<list[j]<list[k] and i<j<k:
            temp=temp+1
print(temp)            
