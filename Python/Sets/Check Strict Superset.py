a = set(map(int, input().split()))
n = int(input())
flag = 0
for i in range(n):
    b = set(map(int, input().split()))
    if len(b.difference(a))==0 and len(a.difference(b)) != 0:
        continue
    else:
        flag =1
        break

if flag==0:
    print(True)
else:
    print(False)
