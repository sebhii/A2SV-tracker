n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

i,j=0,0
arr=[]
while i<n and j<m:
  if a[i]<b[j]:
    arr.append(a[i])
    i+=1
  else:
    arr.append(b[j])
    j+=1
while i<n:
  arr.append(a[i])
  i+=1
while j<m:
  arr.append(b[j])
  j+=1
print(*arr)
