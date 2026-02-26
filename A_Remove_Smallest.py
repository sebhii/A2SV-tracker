t=int(input())
for _ in range(t):
  n=int(input())
  arr=list(map(int,input().split()))
  if n==1:
    print("YES")
    continue
  arr.sort()
  flag=False
  for i in range(1,n):
    if arr[i]-arr[i-1]>1:
      print("NO")
      flag=True
  if(flag):
    continue
  print("YES")