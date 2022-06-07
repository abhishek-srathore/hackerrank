from collections import defaultdict

size = (input().split())
sz_a = int(size[0])
sz_b = int(size[1])
da = defaultdict(list)
st = set()

for i in range(1,sz_a+1):
    da[input().rstrip()].append(i)

for j in range(sz_b):
    s = input().rstrip()
    if len(da[s]) == 0:
        print(-1)
    else:
        for l in range(len(da[s])):
            print(da[s][l], end= " ")
        print()
    