def fib(n):
    return make_list(n)[n-1]

def make_list(n):
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    index = 1
    for i in range(n - 2):
        fib_list.append(fib_list[index] + fib_list[index - 1])
        index += 1
    return fib_list

def main():
    user_in = int(input('\nPlease enter the nth term you want from the sequence: '))
    print("The %ith term of the Fibonacci Sequence is: %i" % (user_in, fib(user_in)))
    print('The Fibonacci Sequence up to that term is: ' + str(make_list(user_in)))
    choice = input('Would you like another? (y/n) ')
    if choice == 'y':
        main()
    quit()

print('\nWelcome to the Fibonacci Calculator!')
main()