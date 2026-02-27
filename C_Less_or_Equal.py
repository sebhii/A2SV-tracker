import sys
n,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
if n<k:
  print(-1)
elif n==k:
  print(arr[n-1])
elif arr[k-1]==arr[k]:
  print(-1)
else:
  print(arr[k-1])
 
