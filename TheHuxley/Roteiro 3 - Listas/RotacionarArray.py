
n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
qr = int(input())
for j in range(n):
    if qr + j < n:
        print(lista[qr + j])
    else:
        print(lista[(qr + j) - n])