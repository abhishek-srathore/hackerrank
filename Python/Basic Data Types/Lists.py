if __name__ == '__main__':
    N = int(input())


    l=[]
   
    for i in range(N):
        data = input().split(sep=' ')
        
        if data[0] == "insert":
            l.insert(int(data[1]), int(data[2]))

        if data[0] == "append":
            l.append(int(data[1]))
        
        if data[0] == "reverse":
            l.reverse()
        
        if data[0] == "print":
            print(l)
        
        if data[0]=="remove":
            l.remove(int(data[1]))
            
        if data[0]=="pop":
            l.pop()
            
        if data[0]=="sort":
            l.sort()
    
