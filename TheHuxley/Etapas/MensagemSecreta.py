n = int(input())

for i in range(n):
    pa = str(input())
    nova = ""
    cont = 0
    for k in range(len(pa)):
        if(pa[k] != " " and cont==0):
            nova += pa[k]
            cont=1
        elif(pa[k-1] == " "):
            cont=0
        elif(pa[k-1] == " " and pa[k-2] == " "):
            cont=0
            if(pa[k] == " " and pa[k+1] == " "):
                cont=0
            elif(pa[k] == " "):
                cont=0
            if(pa[k] == " " and pa[k+1] == " "):
                cont=0
            elif(pa[k] == " "):
                cont=0
        elif(pa[k] == " "):
            cont=0
    print(nova)
