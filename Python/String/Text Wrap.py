import textwrap

def wrap(string, max_width):
    s = ''''''
    c = len(string )%  max_width
    i = 0
    while i <= (len(string)-c-1) :
        s = s + (string[ i: i+max_width])+ "\n"
        i += max_width
    s = s + string[i:]
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)