def minion_game(st):
    count_k = 0
    count_s = 0
    vowel = { 'A','E','I','O','U' }
    
    size = len(st)
    for i in st:
        if i in vowel:
            count_k += size
        else:
            count_s += size
        size -= 1
             
            
      
    if count_s > count_k:
        print("Stuart " + str(count_s))
    elif count_s < count_k:
        print("Kevin " + str(count_k))
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)