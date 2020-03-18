time = str(input())

if(time == "GSW" or time == "HOU" or time == "CLE" or time == "BOS"):
    nome = str(input())
    areten2 = float(input())
    arecon2 = float(input())
    areten3 = float(input())
    arecon3 = float(input())
    est = (arecon2+arecon3)
    peract2 = (arecon2/areten2)
    peract3 = (arecon3/areten3)
    
    if(est > 30):
        print("O time",time,"estah jogando, e",nome,"estah indo bem.")
        
    elif(peract2 > 0.50 and (areten2+areten3)>10):
        print("O time",time,"estah jogando, e",nome,"estah indo bem.")
        
    elif(peract3 > 0.40 and (areten2+areten3)>7):
        print("O time",time,"estah jogando, e",nome,"estah indo bem.")
        
    else:
        print("O time",time,"estah jogando, mas",nome,"nao estah indo bem.")
else:
    print("Nenhum time de interesse jogando.")
