n = int(input())
##qntponto = n
##qntaste = 1
##if(1<= n):
##    for i in range(n):
##        print("." * (qntponto)+("*" * (qntaste)))
##        qntponto -= 1
##        qntaste += 2
##    for i in range(n):
##        if(qntponto == 0):
##            qnt = 1
##        print("." * (qntponto)+("*" * (qntaste)))
##        
##            
##        qntponto += 1
##        qntaste -= 2

qntaste = 1
for i in range(1, n+1):
    for j in range(i, n+1):
        print(".", end='')
    print("*"*(qntaste), end='')
    qntaste +=2
    print()
qntaste = qntaste-2
for i in range(1, n+1):
    for j in range(i):
        
        print(".", end='')
    print("*"*(qntaste), end='')
    qntaste -=2
    print()
        