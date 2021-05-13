N = int(input())
X = list(map(str,input().split()))

x=0
y=0
N -= 1

for i in X:
  if i=='R' and x < N:
    x+=1
  elif i=='L' and x != 0:
    x-=1
  elif i=='U' and y != 0:
    y-=1
  elif i=='D' and y < N:
    y+=1

print(x+1, y+1)
