from math import ceil

def rekt(word, width, height):
    same_word = word
    back_word = word[::-1]
    full_line = ''
    back_line = ''
    for w in range(1, width+1):
        back = (w%2 == 0)
        if back:
            word = word[len(word)-2::-1]
            back_word = back_word[1:]
        elif w > 1 and not back:
            word = word[1:]
            back_word = back_word[len(back_word)-2::-1]
        for c in word:
            full_line += (c + ' ')
        for d in back_word:
            back_line += (d + ' ')
        word = same_word
        back_word = same_word
    full_line = full_line[:len(full_line)-1]   ## To remove the last space
    back_line = back_line[:len(back_line)-1]

    if height == 1:
        real_height = len(word)
    else:
        real_height = (height*len(word))-(height-1)
    e = str(word[1].upper() + '     ')
    kK = str(word[2].upper() + '     ')    ## just k didn't work
    k_list = remove_six(list(range(height*len(word)))[::2])
    count = 0
    for i in range(real_height):
        if i == 0 or i%(len(word)-1) == 0:
            if count%2 == 0:
                print(full_line)
            else:
                print(back_line)
            count += 1
        elif i in k_list:
            for a in range(ceil(width/2)):
                print(kK + e, end='')
            if width%2 == 0:
                print(kK, end='')
            print()
        else:
            for b in range(ceil(width/2)):
                print(e + kK, end='')
            if width%2 == 0:
                print(e, end='')
            print()

def get_primes(n):
    primes = []
    yes = True
    for i in range(2, n+1):
        for a in range(2, i):
            if i%a == 0:
                yes = False
        if yes: primes.append(i)
        yes = True
    return primes  ## NOT print(primes)

def remove_six(lst):
    for a in lst:
        if a%6 == 0:
            lst.remove(a)
    return lst

def main():
    w = input('Enter a four letter word: ').upper()
    wid = int(input('Enter width: '))
    h = int(input('Enter height: '))
    rekt(w, wid, h)
    c = input('\nAgain? ')
    if c != 'n':
        main()
    quit()

main()
