t = int(input())
for j in range(t):
    s = input().rstrip()
    flag = 0
    for i in range(len(s)):
        if s == "/^(?!\.)(?=.)[d-\.]$/":
            print(False)
            flag = 1
            break
        if s[i]== "*" or s[i]=="+":
            if s[i-1]== "*" or s[i-1]=="+":
                print(False)
                flag = 1
                break
                
    
    if flag==0:
        print(True)
                    
