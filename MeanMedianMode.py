from random import randint
from decimal import Decimal

def mean(a):
    dec = int(input("To how many decimal places would you like the mean rounded? "))
    print("The unrounded mean is: " + str(float(sum(a))/len(a)))
    ## print "The rounded mean is: " + str((((float(sum(a))/len(a))*(10**dec))//1)/(10**dec)) <------Works for truncating mean to decimal place, not round
    print("The rounded mean is: " + str(Decimal(str(float(sum(a))/len(a))).quantize(Decimal(str(10**(-dec))))))  ## The str() catser needs to be used, otherwise Decimal adds a whole bunch of funky numbers to the end
    ## Note: Again, I needed the str() around float(sum(a))/len(a) in the above line, otherwise Decimal() added a whole bunch of funky numbers that didn't make sense many places into the decimal
    print('The rounded mean is: %.*f' % (dec, float(sum(a))/len(a)))
    ## Note: It looks like both string formating and quantize work, but formating is quicker.

def median(a):
    temp = sorted(a)
    if len(temp)%2 != 0:
        print("There is one median and it is: " + str(temp[len(temp)/2]))
    else:
        if temp[len(temp)/2-1] == temp[len(temp)/2]:
            print("There is one median and it is: " + str(temp[len(temp)/2]))
        else:
            print("There are two medians and they are: " + str(temp[len(temp)/2-1]) + " and " + str(temp[len(temp)/2]))
            print(str(float(temp[len(temp)/2-1]+temp[len(temp)/2])/2) + " could also be considered the median.")
            ## Very interesting...The number would not float when I had float((temp[len(temp)/2-1]+temp[len(temp)/2])) -- with two parenthesis

## I imported the mode determination from the Java project "USMNames", "MostCommonName" class
## I imported the checking for multiple modes from the Java project "Poker", "Dealer" class
def mode(a):
    count = 0
    max_count = 0
    most = a[0]
    multiple = []
    numModes = 1
    for num1 in a:
        for num2 in a:
            if (num1 == num2):
                count += 1
        if (count > max_count):
            most = num1
            max_count = count
            ## reset
            multiple = []
            multiple.append(most)
            numModes = 1
        elif (count == max_count):
            ## multiple = []  <-------This works for only two modes, but not more because we need to keep the earliest elements
            most = num1
            if not num1 in multiple:
                numModes += 1
                multiple.append(num1)
        count = 0
    if numModes < 2:
        print("There is one mode and it is: " + str(most))
    else:
        print("There are " + str(numModes) + " modes and they are: " + str(sorted(multiple)))

'''
This alternative find_mode(a) is from http://pastebin.com/WUptdUp2

from collections import Counter
from itertools import groupby

def find_mode(a):
    # Group most_common output by freqency
    freqs = groupby(Counter(a).most_common(), lambda x:x[1])
    # Pick off the first group (highest frequency)
    print('Mode(s):', [val for val,count in freqs.__next__()[1]])
'''

def main():
    user_list = []
    print("\nWelcome to the MMMath Operation Station!")
    userin = input("Please enter 1 if you would like to input a list or anything else if you would like to have one randomly generated for you: ")
    user_num = input("Please enter the number of numbers you would like in the list: ")
    if userin == '1':  ## I would do int(input) == 1, but that messes it up me not checking original input for intness
        for i in range(int(user_num)):
            temp_num = input("Please enter element number " + str(i+1) + ": ")
            user_list.append(int(temp_num))
    else:
        max_num = int(input("Please enter the upper limit for the random numbers: "))
        min_num = int(input("Please enter the lower limit for the random numbers: "))
        while (min_num > max_num):
            min_num = int(input("The lower limit can't be higher than the upper limit! Please enter a lower limit: "))  ## Need the int() cast!
        for k in range(int(user_num)):
            user_list.append(int(randint(int(min_num), int(max_num))))  ## uniform() is for floats

    print("Your list of numbers is: " + str(user_list))
    print("Your list of numbers sorted is: " + str(sorted(user_list)))

    mean(user_list)
    median(user_list)
    mode(user_list)

    end()

def end():
    temp = input("Thank you! Would you like another? (y/n) ")
    if temp == 'y':
        main()
    quit()

main()