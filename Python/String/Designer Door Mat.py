l = input().split()
y = int(l[0])
x = int(l[1])
r = x//3
c = r//2

for i in range(0, y//2):
    if i != y//2:      
        for j in range(0, r):
            if j not in range (c-i, c+i+1):
                print("---", end="")
            else:
                print(".|." , end ="")
        print()

for j in range(0, r):
    if j not in range (c-1, c+2):
        print("---", end="")
    elif j== c-1:
        print("-WE",end="")
    elif j== c:
        print("LCO",end="")
    elif j== c+1:
        print("ME-",end="")
print()

for i in range(y//2,-1,-1):
    if i != y//2:      
        for j in range(0, r):
            if j not in range (c-i, c+i+1):
                print("---", end="")
            else:
                print(".|." , end ="")
        print(" ")    
            

        
        

