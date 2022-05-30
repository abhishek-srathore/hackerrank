from itertools import combinations
a = input().split()
v = int(a[1])
l = []

for _ in a[0]:
    l.append(_)
l.sort()
for i in range(1,v+1):
    p = list(combinations(l, i ))
    for j in p:
        st=""
        for z in j:
            st= st+z
        print(st)
