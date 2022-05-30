def mutate_string(string, position, character):
    l =[]
    for i in string:
        l.append(i)
    l[position] = character
    st = "".join(l)
    return st

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)