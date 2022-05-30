n = int(input())
s = set(map(int, input().split()))
m= int(input())
for i in range(m):
    task= input().split()
    if task[0] == "pop":
        s.pop()
    elif task[0] == "discard":
        s.discard(int(task[1]))
    elif task[0] == "remove":
        s.remove(int(task[1]))
    else:
            pass
sum = 0
for i in s:
    sum += i
print(sum)
            
    
