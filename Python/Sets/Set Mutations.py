# Enter your code here. Read input from STDIN. Print output to 
# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
l1 = input().split(" ")
s1 = set(l1)
fun  = int(input())
sum = 0
i =0
while i < fun :
    n = input().split(" ")
    
    if n[0] == "update":
        l2 = input().split(" ")
        s2 = set(l2)
        s1 |= s2
        a= len(s1)
        
    if n[0] == "symmetric_difference_update":
        l2 = input().split(" ")
        s2 = set(l2)
        s1 ^= s2
        a= len(s1)
        
    if n[0] == "difference_update":
        l2 = input().split(" ")
        s2 = set(l2)
        s1 -= s2
        a= len(s1)
        
    if n[0] == "intersection_update":
        l2 = input().split(" ")
        s2 = set(l2)
        s1 &= s2
        a= len(s1)
    sum += a
    i+=1
add=0
for i in s1:
    add += int(i) 
print(add)

        
