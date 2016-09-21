def make_table(num):
    print()
    for i in range(1, num+1):
        for k in range(1, num+1):
            print('%5i' % (k*i), end="")  ## Using string.rjust() could also be used here -- Look below
        print()

# Another way to make the table, with correct spacing in between the numbers
# maxval=int(input("Choose your highest number: "))
# maxlength = len(str(maxval**3))
# for i in range(1, maxval + 1):
#     for j in range(1, maxval + 1):
#         print(str(j*i).rjust(maxlength,' '), end='')
#     print()

def main():
    print('\nWelcome to the Table Maker!')
    num = int(input("Please enter the size of the table: "))
    make_table(num)
    choice = input("\nWould you like to make another? (y/n) ")
    if choice == 'y':
        main()
    quit()

main()
