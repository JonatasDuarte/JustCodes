falhas = ['1' , '3', '4', '5']
certos = ['i', 'e', 'a', 's']

while(True):
    pa = str(input())
    res = " "*len(pa)
    for i in range(len(pa)):
        if(pa[i] in falhas):
            for k in range(len(falhas)):
                if(pa[i] == falhas[k]):
                    res = res[0:i] + certos[k] + res[i:]
                    break
        else:
            res = res[0:i] + pa[i] + res[i:]
    res = res.upper()
    res = res[:len(pa)]
    
    if(res == "FIM" or res == "SAIR"):
        break
    else:
        print(res)