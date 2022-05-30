from itertools import combinations_with_replacement
a = input().split()
v = int(a[1])
l = []

for _ in a[0]:
    l.append(_)
l.sort()

p = list(combinations_with_replacement (l, v ))
for j in p:
    st=""
    for z in j:
        st= st+z
    print(st)
