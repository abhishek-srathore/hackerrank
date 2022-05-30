def print_rangoli(size):

    al = 96 + size

    for i in range(size):
        str= []
        r = 1+(4*i)
        j= 0
        c = 0
        flag = 0
        while j<r:
            if j%2 ==0:
                str.append(chr(al-c))
                if c<=i+1 and flag == 0:
                    c += 1
                    if c == i:
                        flag =1   
                else:
                    c -= 1
                j+= 1
                
            else:
                str.append("-")
                j+=1
        print("".join(str).center(4*(size-1)+1,"-"))
        
    for i in range(size-2, -1, -1):
            str= []
            r = 1+(4*i)
            j= 0
            c = 0
            flag = 0
            while j<r:
                if j%2 ==0:
                    str.append(chr(al-c))
                    if c<=i+1 and flag == 0:
                        c += 1
                        if c == i:
                            flag =1   
                    else:
                        c -= 1
                    j+= 1
                    
                else:
                    str.append("-")
                    j+=1
            print("".join(str).center(4*(size-1)+1,"-"))
                
                               
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)