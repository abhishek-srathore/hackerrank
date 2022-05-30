from itertools import groupby
data = input()
F = []
groups = []
uniquekeys = []
for k, g in groupby(data, None):
    groups.append(list(g))     
    uniquekeys.append(k)
    print((len(groups[-1]), int(k)), end=" ")
    
