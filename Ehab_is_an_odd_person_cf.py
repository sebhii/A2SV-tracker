n=int(input())
arr=list(map(int,input().split()))
eve=0
odd=0

for num in arr:
  if num%2:
    odd+=1
  else:
    eve+=1
if odd and eve:
  arr.sort()
print(*arr)
