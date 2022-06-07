from collections import OrderedDict

dic = OrderedDict()
k = int(input())
for i in range(k):
    s = input().split()
    if len(s) == 2:
        dic[s[0]] = dic.get(s[0], 0)+int(s[1])
    else:
        t =s[0]+" "+s[1]  
        dic[t] = dic.get(t, 0) +int(s[2])
        
for k in dic:
    print(k, dic[k])       
