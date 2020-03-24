mk = 0
cmren = " "
while True:
    nc = input()
    if nc.upper() == "FIM":
        break
    km = int(input())
    val = float(input())
    if (km > mk) and (val * 2 <= 300):
        cmren = nc.upper()
        mk = km
if (cmren == " "):
    print("SEM DESTINO")
else:
    print(cmren)