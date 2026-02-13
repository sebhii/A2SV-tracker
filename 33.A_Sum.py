t=int(input())
for i in range(t):
  a,b,c=map(int,input().split())
  maxi=max(a,b,c)
  sum=a+b+c
  print("YES" if sum-maxi==maxi else "NO")