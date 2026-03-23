n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

arr=[]
i=0
for num in b:

  while i<n and num > a[i]:
    i+=1
  arr.append(i)
print(*arr)
