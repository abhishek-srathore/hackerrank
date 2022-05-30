from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

c = list(product(a,b))

for i in range(len(c)):
    print(c[i], end = " ")
