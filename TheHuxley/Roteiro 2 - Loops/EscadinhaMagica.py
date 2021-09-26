n = int(input())
for x in range(1,n+1):
    for y in range(1, x+1):
      if y==x:
        print(y, end='')
      else:
        print(y, end=' ')
    print()
