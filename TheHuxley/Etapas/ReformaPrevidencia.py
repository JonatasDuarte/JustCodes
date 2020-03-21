tt = str(input())

if(tt != "PV" and tt != "TR" and tt != "SP" and tt != "PR" and tt != "PC"):
    print("Categoria de trabalhador invalida.")
    
else:
    sexo = str(input())
    ida = int(input())
    tc = int(input())

    #Trabalhador privado
    if(tt == "PV"):
        if(tc >= 20):
            if(sexo == "M" or sexo == "m"):
                if(ida >= 65):
                    print("Trabalhador Privado pode se aposentar.")
                else:
                    print("Trabalhador Privado NAO pode se aposentar!")

            elif(sexo == "F" or sexo == "f"):
                if(ida >= 62):
                    print("Trabalhador Privado pode se aposentar.")
                else:
                    print("Trabalhador Privado NAO pode se aposentar!")
        else:
            print("Trabalhador Privado NAO pode se aposentar!")

    #Trabalhador rurais
    elif(tt == "TR"):
        if(tc >= 20):
            if(ida >= 60):
                print("Trabalhador Rural pode se aposentar.")
            else:
                print("Trabalhador Rural NAO pode se aposentar!")
        else:
            print("Trabalhador Rural NAO pode se aposentar!")

    #Servidor publico
    elif(tt == "SP"):
        tp = int(input())
        ts = int(input())
        if(sexo == "M" or sexo == "m"):
            if(ida >= 65):
                if(tc >= 25):
                    if((tp >= 10) and (ts >= 5)):
                        print("Servidora publica pode se aposentar.")
                    else:
                        print("Servidor publico NAO pode se aposentar.")
                else:
                    print("Servidor publico NAO pode se aposentar.")
            else:
                print("Servidor publico NAO pode se aposentar.")
                
        elif(sexo == "F" or sexo == "f"):
            if(ida >= 62):
                if(tc >= 25):
                    if((tp >= 10) and (ts >= 5)):
                        print("Servidora publica pode se aposentar.")
                    else:
                        print("Servidor publico NAO pode se aposentar.")
                else:
                    print("Servidor publico NAO pode se aposentar.")
            else:
                print("Servidor publico NAO pode se aposentar.")

    #Professor
    elif(tt == "PR"):
        if(tc >= 30):
            if(ida >= 60):
                print("Professor pode se aposentar.")
            else:
                print("Professor NAO pode se aposentar!")
        else:
            print("Professor NAO pode se aposentar!")

    #Policiais
    elif(tt == "PC"):
        if(ida >= 55):
            tf = int(input())
            
            if(sexo == "M" or sexo == "m"):
                if((tf >= 20) and (tc >= 30)):
                    print("Policial pode se aposentar.")
                else:
                    print("Policial NAO pode se aposentar!")
            
            elif(sexo == "F" or sexo == "f"):
                if((tf >= 15) and (tc >= 25)):
                    print("Policial pode se aposentar.")
                else:
                    print("Policial NAO pode se aposentar!")
        else:
            print("Policial NAO pode se aposentar!")
                    