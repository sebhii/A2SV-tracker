n,s=map(int,input().split())
a=list(map(int,input().split()))
sm=0
maxi=0
left=0
for right in range(n):
  sm+=a[right]
  while sm>s:
    sm-=a[left]
    left+=1
  maxi=max(maxi,right-left+1)
print(maxi)
