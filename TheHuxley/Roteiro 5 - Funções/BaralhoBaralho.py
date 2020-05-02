paes = input().split()
wili = input().split()
paes.sort()
wili.sort()
pa = 0
wi = 0
  
if(int(paes[0]) == int(paes[1]) and int(paes[1]) == int(paes[2])):
    pa += int(paes[0])
elif((int(paes[0]) == int(paes[1]))):
    pa += int(paes[0])//2
elif(paes[1] == paes[2]):
    pa += int(paes[1])//2
    
if(int(paes[2]) - int(paes[1]) == 1 and int(paes[1])-int(paes[0]) == 1):
    pa += int(paes[0])
if(int(paes[0]) + int(paes[1]) + int(paes[2]) == 8):
    pa += 8

if(int(wili[0]) == int(wili[1]) and int(wili[1]) == int(wili[2])):
    wi += int(wili[0])
elif((wili[0] == wili[1])):
    wi += int(wili[0])//2
elif(wili[1] == wili[2]):
    wi += int(wili[1])//2
    
if(int(wili[2]) - int(wili[1]) == 1 and int(wili[1]) - int(wili[0]) == 1):
    wi += int(wili[0])
if(int(wili[0]) + int(wili[1]) + int(wili[2]) == 8):
    wi += 8

if(wi > pa):
    print(int(2))
elif(pa > wi):
    print(int(1))
else:
    print(int(0))

