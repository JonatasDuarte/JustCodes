n = int(input())
quebrou = 0

for i in range(1, n+1):
    ban = input().split(" ")
    
    if(int(ban[0]) > int(ban[1])):
        quebrou += int(ban[1])

print(quebrou)

