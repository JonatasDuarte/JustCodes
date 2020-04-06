n = int(input())
l1, l2, l3 = [], [], []

for i in range(n):
    l1.append(int(input()))

for i  in range(n):
    l2.append(int(input()))

for i in range(n):
    l3.append(l1[i])
    l3.append(l2[i])

for i in range(len(l3)):
    print(l3[i])
