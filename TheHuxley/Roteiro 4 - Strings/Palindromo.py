n = int(input())
novo = ""

for i in range(n):
    frase = str(input())
    frase = frase.replace(" ","")
    frase = frase.upper()
    novo = frase[::-1]
    if(frase == novo):
        print("SIM")
    else:
        print("NAO")