op = str(input())

if(op != "a")and(op != "p")and(op != "h"):
    print("Escolha um tipo de media valida.")
else:
    if(op == "a"):
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        media = (n1+n2+n3)/3
        if(70 <= media <= 100):
            print("%.2f" % media)
            print("Aprovado")
            
        elif(40 < media < 70):
            print("%.2f" % media)
            print("Final")
            
        elif(0 <= media <= 40):
            print("%.2f" % media)
            print("Reprovado")
            
        else:
            print("Media invalida")
                  
    elif(op == "p"):
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        p1 = int(input())
        p2 = int(input())
        p3 = int(input())
        media = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
        
        if(70 <= media <= 100):
            print("%.2f" % media)
            print("Aprovado")
            
        elif(40 < media < 70):
            print("%.2f" % media)
            print("Final")
            
        elif(0 <= media <= 40):
            print("%.2f" % media)
            print("Reprovado")
            
        else:
            print("Media invalida")
                  
    elif(op == "h"):
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        media = 3/((1/n1)+(1/n2)+(1/n3))
        if(70 <= media <= 100):
            print("%.2f" % media)
            print("Aprovado")
            
        elif(40 < media < 70):
            print("%.2f" % media)
            print("Final")
            
        elif(0 <= media <= 40):
            print("%.2f" % media)
            print("Reprovado")
            
        else:
            print("Media invalida")


    
