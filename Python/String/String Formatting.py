def print_formatted(number):
    blen = len(str(bin(number))[2:])
    
    for i in range(1,number+1):
        print(str(i).rjust(blen," "), str(oct(i))[2:].rjust (blen," "), str(hex(i))[2:].rjust(blen," "), str(bin(i))[2:].rjust(blen," "), sep= " ")
        
       
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)