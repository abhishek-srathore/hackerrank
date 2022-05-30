m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))

print(len(e.union(f)))
