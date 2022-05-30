

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
l= []   
s = a.symmetric_difference(b)
for i in s:
    l.append(i)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
for j in l:
    print(j)
