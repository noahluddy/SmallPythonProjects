def make_change():
    money = input("Please enter how much money you have: ")

    ## I need this while loop because isdigit() returns False for floating point numbers
    while (True):
        try:
            float(money)
            break
        except ValueError:
            money = input("You did not enter a number. Please enter a number: ")

    money = (((float(money)*100)//1)/100)  ## Converts number to two decimal places -- doesn't round, though :(
    initial_money = money
    quarters = int(money // 0.25)
    money %= 0.25
    dimes = int(money // 0.1)
    money %= 0.1
    nickels = int(money // 0.05)
    money %= 0.05
    pennies = int(money // 0.01)
    total_coins = quarters + dimes + nickels + pennies

    print("\n$" + str(initial_money) + " comes to\n" + str(quarters) + " quarters\n" + str(dimes) + " dimes\n" + str(nickels) + " nickels\n" + str(pennies) + " pennies\n\n" + str(total_coins) + " total coins")
    end()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)  ## For non-Arabic numbers
        return True
    except (TypeError, ValueError):
        pass
    return False

def end():
    user_in = input("\nWould you like to enter more change? (y/n) ")
    if user_in == 'y':
        make_change()
    quit()

print "Welcome to the Change Calculator!"
make_change()
