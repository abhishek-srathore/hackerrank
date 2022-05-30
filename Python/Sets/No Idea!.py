l = input().split(" ")
n = int(l[0])
m = int(l[1])

a = input().split(" ")
s1 = set(input().split(" "))
s2 = set(input().split(" "))

h = 0
for i in a:
    if i in s1:
        h+=1
    elif i in s2:
        h-=1
    else:
        pass
    
print(h)
        
