from collections import OrderedDict

dic  = {}
k = int(input())
for i in range(k):
    s = input().strip()
    dic[s] = dic.get(s,0) +1

print(len(dic.keys()))
for i in dic:
    print(dic[i], end = " ")
