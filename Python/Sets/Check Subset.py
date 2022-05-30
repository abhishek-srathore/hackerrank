t = int(input())
for i in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    
    if len(a.difference(b))==0:
        print(True)
    else:
        print(False)
