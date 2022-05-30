if __name__ == '__main__':
    st = input()
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False


    for i in st:
        if flag4 == False and  i.isdigit() :
            flag4 = True

        elif i.isalpha():
            flag1 = True
            if not flag3 or not flag2:
                if flag2 == False and  i.islower() :
                    flag2 = True
                if flag3 == False and i.isupper():
                    flag3 = True
        
            
                    


    print(flag1 or flag4)
    print(flag1)
    print(flag4)
    print(flag2)
    print(flag3)
        

