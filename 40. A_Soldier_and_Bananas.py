k,n,w=map(int,input().split())
s=0
for i in range(1,w+1):
  s+=i*k

debt=s-n
if(debt<0):
  print(0)
else:
  print(debt)