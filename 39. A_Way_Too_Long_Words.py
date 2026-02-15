n=int(input())
for i in range(n):
  word=input()
  ln=len(word)
  if(ln<=10):
    print(word)
    continue
  ln-=2
  st=""
  st+=word[0]
  st+=str(ln)
  st+=word[-1]
  print(st)