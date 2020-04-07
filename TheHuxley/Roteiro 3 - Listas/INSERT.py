l, res, resf = [], "[ ", "[ "
n = int(input())
for i in range(n):
    item = input()
    l.append(int(item))
    res+= item+" "
res+="]"
pos = int(input())
val = int(input())
print(res)
if(pos>n):
    print("A posicao "+str(pos)+" estah fora do intervalo")
else:
    l = l[:(pos)] + [val] + l[pos:]
    for j in range(n+1):
        resf += str(l[j])+" "
    resf+= "]"
    print(resf)