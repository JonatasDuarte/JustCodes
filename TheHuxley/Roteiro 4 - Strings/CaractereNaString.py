palavra = str(input())
letra = str(input())
cont = 0

for i in range(len(palavra)):
    if(palavra[i] == letra):
        cont += 1

print(cont)
