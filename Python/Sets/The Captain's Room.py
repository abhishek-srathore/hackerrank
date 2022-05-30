n = int(input())
l = list(map(int, input().split()))
s1 = set()
s2 = set()

for i in l:
    if i not in s1:
        s1.add(i)
    else:
        s2.add(i)
s3 = s1.difference(s2)
for i in s3:
    print(i)
