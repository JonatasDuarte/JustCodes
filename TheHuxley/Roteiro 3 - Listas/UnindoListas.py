n1 = int(input())
if(n1 == 0):
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    l1 = []
    for i in range(1, n1+1):
        v1 = int(input())
        l1.append(v1)

    n2 = int(input())
    if(n2 ==0):
        print("Erro - A lista deve ter pelo menos 1 elemento.")

    else:
        l2 = []
        for i in range(1, n2+1):
            v2 = int(input())
            l2.append(v2)

        if((len(l1) == 0 or len(l2) == 0)):
           print("Erro - A lista deve ter pelo menos 1 elemento.")
        else:
            res = str(l1+l2)
            res = res.replace(",","")
            res = res.strip("[")
            res= res.strip("]")
            print(res)
            

