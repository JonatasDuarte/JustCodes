pa = str(input())
pa = pa.split()
par = False
for i in range(len(pa)):
    if(par):
        pa[i] = (pa[i])[::-1]
        par = False
    else:
        par = True
        
print(" ".join(pa))