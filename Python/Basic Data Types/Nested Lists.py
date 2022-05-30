if __name__ == '__main__':
    l=[]
    m = 1000000000000000000000
    c = 1000000000000000000000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        m = min(score, m)
        
    count = 0    
    for i in l:
        if i[1] == m:
            pass
        else:
            c = min(i[1],c)
        count += 1
    
    final = []
    for j in l:
        if j[1] == c:
            final.append(j[0])
    final.sort()
    for t in final:
        print(t)
            
        
