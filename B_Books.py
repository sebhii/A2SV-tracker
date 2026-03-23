n,t=map(int,input().split())
a=list(map(int,input().split()))
left=0
s=0
maxi=0
for right in range(n):
  s+=a[right]
  while s>t:
    s-=a[left]
    left+=1
  maxi=max(maxi,right-left+1)
print(maxi)
