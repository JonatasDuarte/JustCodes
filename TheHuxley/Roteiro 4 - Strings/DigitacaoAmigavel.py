amg = ["0", "1", "2","3","4","5","6","7","8","9","o","O","l"]
num = ""
while(num != "FIM"):
    amigavel = True
    num = input()
    if(num.upper() == "FIM"):
        break

    if("l" in num):
        num = num.replace("l", "1")
    if("O" in num):
        num = num.replace("O", "0")
    if("o" in num):
        num = num.replace("o", "0")
        
    for i in range(len(num)):
        if not (num[i] in amg):
            amigavel = False
            
    if(amigavel):
        print(int(num))
        
    else: 
        print("ERRO")