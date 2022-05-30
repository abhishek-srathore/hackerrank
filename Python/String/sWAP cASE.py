def swap_case(s):
    st = ""
    for i in s:
        a = ord(i)
        if  a >= 65  and a <= 90:
            st = st + chr(a+32)
        elif a >= 91   and a <=122 :
            st = st + chr(a-32)
        else:
            st = st+ i
        
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)