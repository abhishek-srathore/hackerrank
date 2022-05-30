def split_and_join(line):
    # write your code here
    l = line.split()
    st = "-".join(l)
    return st

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)