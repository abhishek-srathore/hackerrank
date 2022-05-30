from collections import Counter

x = int(input())
size = input().split()

avail = Counter(size)

costumers = int(input())
total = 0
for i in range(costumers):
    cos_it =  input().split()
    cos_siz = cos_it[0]
    cos_amt = cos_it[1]
    if avail[cos_siz] > 0:
        avail[cos_siz] -= 1
        total += int(cos_amt)
print(total)
        
        
    

