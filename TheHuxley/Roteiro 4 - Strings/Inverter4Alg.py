n = int(input())
n = str(n)
n = n[::-1]

for i in range(len(n)):
    if(n[i] != "0"):
        print(n[i], end="")
        