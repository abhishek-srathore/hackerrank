from itertools import permutations

a = input().split()
k = int(a[1])
l = []

for i in a[0]:
    l.append(i)
l.sort()
st =""

c = list(permutations(l,k))


j = 0
while j < len(c):
    print("".join(c[j]))
    j+=1
    
    
    
    
