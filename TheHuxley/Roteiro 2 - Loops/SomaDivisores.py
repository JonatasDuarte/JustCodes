n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0

for i in range(1,n1+1):
    if(n1%i == 0):
        t1 += i
for i in range(1,n2+1):
    if(n2%i == 0):
        t2 += i
for i in range(1,n3+1):
    if(n3%i == 0):
        t3 += i
for i in range(1,n4+1):
    if(n4%i == 0):
        t4 += i
for i in range(1,n5+1):
    if(n5%i == 0):
        t5 += i
        
if(t1>=t2 and t1>=t3 and t1>=t4 and t1>=t5):
    print(n1)
elif(t2>=t1 and t2>=t3 and t2>=t4 and t2>=t5):
    print(n2)
elif(t3>=t2 and t3>=t1 and t3>=t4 and t3>=t5):
    print(n3)
elif(t4>=t2 and t4>=t3 and t4>=t1 and t4>=t5):
    print(n4)
else:
    print(n5)
    
