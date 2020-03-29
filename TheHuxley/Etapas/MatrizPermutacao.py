soma =0
pos= 0
cont=0
co = 0
nm = True
res = True
k = ""
n = int(input())
lin = input().split()
for i in range(len(lin)):
    soma += int(lin[i])
    if(int(lin[i]) == 1):
        pos = i
        cont +=1
    if((pos+n <= len(lin)) and cont<n):
        if(int(lin[pos+n]) >= 1):
            nm = False

for i in range(len(lin)):
    co +=1 
    if(co<n):
        k += str(lin[i])+" "
    elif(co == n):
        k += str(lin[i])+" "
        k += "\n"
        co=0        

if(soma > n or nm == False):
    print(k[:-1])
    print("False")
else:
    print(k[:-1])
    print("True")


