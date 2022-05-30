t = int(input())
for i in range(t):
    try:
        
        n = input().split()
        b = int(n[1])
        a = int(n[0])
        
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e :
        print("Error Code:", e)
 

    
