#############################################################################################################################################
#                                                                                                                                           #
# For this assignment you will create and test 10 functions in Python.                                                                      #
# The 10 functions that you must create and test are described in detail below.                                                             #
# Be sure that you take  input provided by function 10 for all of your other function arguments!                                            #
# If you do not, you cannot properly test them and neither can your professor to properly grade your assignment!                            #
# Be sure to use comments for both structure of the program and documentation of the code.                                                  #
# All code must completely be your own individual work product.                                                                             #
# You may also create and use additional functions to                                                                                       #
#     help with the responsibilities of the ten required functions if you wish.                                                             #
# All 10 of these required functions should be included in a single .py file. Post your .py file here.                                      #
#                                                                                                                                           #
# 1. A function that displays your name and your major at UAT. The output should look like this:                                            #
#       Name: Drale Glacen                                                                                                                  #
#       Major: Advancing Computer Science                                                                                                   #
# 2. A function that prompts the user to enter their age and returns the user's input as an int                                             #
# 3. A function that takes one argument - the argument will be a name that is a string.                                                     #
#       The function will display a message like this:                                                                                      #
#           Hello Drale Glacen!                                                                                                             #
# 4. A function that takes an integer argument called number and returns the inverse of that number.                                        #
#       For example, if you pass it 3, it will return -3, and if you pass it -3 it will return 3                                            #
#       (see improved function below for validating int input to include negative ints).                                                    #
# 5. A function that takes an integer argument called count and a string argument called message.                                           #
#       The function will display the message <count> times.                                                                                #
#       For example, if the message is "Hello!" and the count is 3, then the functions will display "Hello!" three times.                   #
# 6. A function called getBiggest that takes two int arguments called num1 and num2.                                                        #
#       The function will return the largest of the two argument values.                                                                    #
#       If the arguments are equal, then it will return the first argument value.                                                           #
# 7. A function that takes a string argument and counts and returns the number of capital letters in the argument string.                   #
#       For example, if the argument value is "My name is Albert Einstein.", then the return value will be 3.                               #
# 8. A function that takes three int arguments and returns the middle value.                                                                #
#       For example, if the argument values are 5, 3, and 4, then the function will return 4.                                               #
#           If there is no middle value then the function will return the most common value.                                                #
#           For example, if the argument values are 5, 3, and 5, then the function will return 5.                                           #
# 9. A function that takes two string arguments and returns a string with only the characters that are in both of the argument strings.     #
#    There should be no duplicate characters in the return value.                                                                           #
#       For example, if the two argument values are "spaghetti" and "shipping" then the function should return "spghi"                      #
#       (or any five character string with these five characters that are common to both argument strings).                                 #
# 10. A function that calls each of the functions above in order to show that they work correctly and provides all data to run them         #
#       so the user of the main program doesn't have to provide inputs for the other 9 functions.                                           #
#                                                                                                                                           #
#############################################################################################################################################

import string

def validPosInput(x):                                                                                                   # checks for valid input and turns it into an int                                                    
    while True:                                                                                                         # this won't accept negative numbers   
        if (str.isdigit(x)):                                                                                            
            x = int(x)                                                                                                  
            break                                                                                                       
        else:                                                                                                           
            x = input('Please select a valid positive integer\n')                                                                
    return x                                                                                                            

def validInput(x):                                                                                                      # checks for valid input and turns it into an int                                                    
    while True:                                                                                                         # this accepts negative variables by stripping the '-'
        if (x.lstrip('-').isdigit()):                                                                                   
            x = int(x)                                                                                                  
            break                                                                                                       
        else:                                                                                                           
            x = input('Please select a valid integer\n')                                                                
    return x

def nameMajor(name, major):                                                                                             # Prints both the users name and the users major
    print('Name:', name)
    print('Major:', major)
    return()

def userAge(age):                                                                                                       # Prints the users age
    print ('Age: ', age)
    return()

def helloName(name):                                                                                                    # Prints hello and then the users name
    print('Hello', name)
    return()

def inverse(invertNum):                                                                                                 # gets the inverse of any number you the user selects
    invertNum = int(invertNum)
    invertNum = -(invertNum)
    print('Your inverted number is: ',invertNum)
    return()

def showNumTimes(message, repeatMessage):                                                                               # gets the message the user selected and print it the number of times the user told us to repeat it
    repeatMessage = int(repeatMessage)
    for i in range (repeatMessage):
        print(message)
    return()

def getBiggest(num1, num2):                                                                                             # Get the biggest number between the two variables and return it
    if (num1 > num2):
        return(num1)
    elif(num1 < num2):
        return(num2)
    elif(num1==num2):
        return(num1)
    
def capitalLetters(capitals):                                                                                           # Check for capital letters in a string and return the number of capital letters
    numCapitals = 0
    for c in (capitals):
        if(c.isupper()):
            numCapitals += 1
    return(numCapitals)

def middleValue(midNum1, midNum2, midNum3):                                                                             # Find number in the middle of 3 different variables, if 2 numbers are equal print the common variable
    if ((midNum1 < midNum2 < midNum3) or (midNum3 < midNum2 < midNum1)):                                                # and return the middle number
        return (midNum2)
    elif ((midNum3 < midNum1 < midNum2) or (midNum2 < midNum1 < midNum3)):
        return (midNum1)
    elif ((midNum1 < midNum3 < midNum2) or (midNum2 < midNum3 < midNum1)):
        return (midNum3)
    elif ((midNum1 == midNum2) or (midNum1 == midNum3)):
        return (midNum1)
    elif ((midNum2 == midNum3) or (midNum2 == midNum1)):
        return (midNum2)
    elif ((midNum3 == midNum1) or (midNum3 == midNum2)):
        return (midNum3)
    
def inBoth(string1, string2):                                                                                           # Check if both string1 and string2 share common letters
    stringList = []                                                                                                     # if they do return the shared letters as a string
    for c in (string1):
        if c in string2:
            if c not in stringList:
                stringList.append(str(c))
    sameChar = ''.join(stringList)
    return(sameChar)
    
def main():
    
# Name & Major
    name = input('What is your name? ')                                                                                 # gets users name and stores that into the name variable
    major = input('What is your Major at UAT? ')                                                                        # gets users major and stores that into the major variable
    nameMajor(name, major)                                                                                              # calls the function nameMajor
# Age
    age = input('How old are you? ')                                                                                    # gets users age and sotres that into the age variable
    age = (validPosInput(age))                                                                                          # Assigns age to the return of validPosInput
    userAge(age)                                                                                                        # calls the function userAge  
# Hello Name
    helloName(name)                                                                                                     # calls the function helloName
# Invert Numbers
    invertNum = input('Please select a number to invert ')                                                              # gets a number from the user and stores that into the invertNum variable
    invertNum = (validInput(invertNum))                                                                                 # assign the return of validInput to invertNum
    inverse(invertNum)                                                                                                  # calls the inverse function
# Repeat Message
    message = input('What is your favorite saying? ')                                                                   # gets a message from the user and stores that into the message variable
    repeatMessage = input('How many times would you like to repeat your saying? ')                                      # gets a number from the user and stores that into the repeatMessage variable
    repeatMessage = (validPosInput(repeatMessage))                                                                      # Assigns the return of validPosInput to the repeatMessage variable
    showNumTimes(message, repeatMessage)                                                                                # calls showNumTimes function
# Biggest Number
    num1 = input('Please select a number for biggest number ')                                                          # gets a number from the user and stores that into num1 variable                                                                                               
    num1 = (validInput(num1))                                                                                           # Assigns num1 to the return of validInput
    num2 = input('Please select a number for biggest number ')                                                          # gets a number from the user and sotres that into num2 variable
    num2 = (validInput(num2))                                                                                           # Assigns num2 to the return of validInput
    getBiggest(num1, num2)                                                                                              # calls getBiggest function
    print('Big Number is: ', getBiggest(num1, num2))                                                                    # displays return of getBiggest function
# Number of Capital Letters
    capitals = input('Please make a statement using a variety of capital and lower case letters. \n')                   # gets a statement for evaluation and stores that into the capitals variable
    capitalLetters(capitals)                                                                                            # calls capitalLetter function
    print('There are', capitalLetters(capitals),'capital letters in your statement.')                                   # print the return of the capitalLetters function
# Middle Number is...
    midNum1 = input('Please select a number at random ')                                                                # gets a number from the user and stores it into the midNum1 variable
    midNum1 = (validInput(midNum1))                                                                                     # Assigns midNum1 to the return of validInput
    midNum2 = input('Please select another number at random ')                                                          # gets a number from the user and stores it into the midNum2 variable
    midNum2 = (validInput(midNum2))                                                                                     # Assigns midNum2 to the return of validInput
    midNum3 = input('Please select yet another number at random ')                                                      # gets a number from the user and stores it into the midNum3 variable
    midNum3 = (validInput(midNum3))                                                                                     # Assigns midNum3 to the return of validInput
    middleValue(midNum1, midNum2, midNum3)                                                                              # calls function middleValue
    print('Middle value is: ', middleValue(midNum1, midNum2, midNum3))                                                  # gets the result from middleValue and displays the middle value
# Shared Numbers
    string1 = input('Tell me something about yourself \n')                                                              # gets something from user and assigns it to the string1 variable
    string2 = input('Tell me something else about yourself \n')                                                         # gets something from user and assigns it to the string2 variable
    inBoth(string1, string2)                                                                                            # calls the inBoth function
    print('These letters are shared between your two "about yourself statements" \n', inBoth(string1, string2), sep='') # displays the return of the inBoth function
#Close program line
    close = input('Press ENTER to close program')                                                                       # This just closes your program when it is finished running after you press ENTER

main()                                                                                                                  # This calls the main function
