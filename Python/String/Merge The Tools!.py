def merge_the_tools(string, k):
    i = 0
    while i+k <= len(string): 
        str= ""
        st = string[i:i+k]
        for j in st:
            if j not in str:
                str = str+j
        print(str)
        i += k
        
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)