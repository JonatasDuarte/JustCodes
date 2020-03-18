crime = str(input())
if(crime == "tr�fico" or crime == "roubo"):
    valc = int(input())

if(crime != "homic�dio" and crime!="tr�fico" and crime !="roubo"):
    print("Crime inv�lido.")
else:
    dela = str(input())
    if(dela == "tr�fico" or dela == "roubo"):
        vald = int(input())
            
    if(dela != "homic�dio" and dela!="tr�fico" and dela !="roubo"):
        print("Crime inv�lido.")
    
    else:

        if(crime == "roubo"):
            if(dela == "homic�dio"):
                print("Dela��o concedida.")
                
            elif(dela == "roubo"):
                if(vald >(valc*5) ):
                    print("Dela��o concedida.")
                else:
                    print("Dela��o rejeitada.")
                    
            elif(dela == "tr�fico"):
                if(vald >(valc*3) ):
                    print("Dela��o concedida.")
                else:
                    print("Dela��o rejeitada.")
            else:
                print("Dela��o rejeitada.")
                    
        elif(crime == "tr�fico"):
            if(dela == "homic�dio"):
                print("Dela��o concedida.")
                
            elif(dela == "tr�fico"):
                if(vald >(valc*5) ):
                    print("Dela��o concedida.")
                else:
                    print("Dela��o rejeitada.")
            else:
                print("Dela��o rejeitada.")
                    
        elif(crime == "homic�dio"):
            if(dela == "homic�dio"):
                print("Dela��o concedida.")
            else:
                print("Dela��o rejeitada.")

