def count_substring(string, sub_string):
    i = 0
    count= 0 
    while i+len(sub_string)<len(string)+1:
        if sub_string==string[i:i+len(sub_string)]:
            count= count +1
        i=i+1
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)