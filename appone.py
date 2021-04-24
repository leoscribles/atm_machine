import random

import time
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
time = str(current_time)

from datetime import date
date = str(date.today())

database = {}

def init():
    print('Welcome to Bank Zuri')
    haveAccount = int(input('Do you have an account with us?\n1.Yes\n2.No\n'))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print('Invalid option selected. Please try again.')
        init()

def login():
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountNumberFromUser = int(input('Input your account number \n'))
        password = input('What is your password?\n')
        for accountNumber, userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    isLoginSuccessful = True
    bankOperations(userDetails)

def register():
    email = input('what is your email address? \n')
    firstName = input('what is your first name? \n') 
    lastName = input('what is your last name? \n')
    password = input('create a password for yourself \n')

    accountNumber = generateAccount()
    userDetails = [firstName, lastName, email, password]
    database[accountNumber] = userDetails

    print('Your account has been created')
    print('=============================')
    print('Your account number is %s' % accountNumber)
    print('Copy it and save it')
    print('=============================')

    login()

def bankOperations(userDetails):
    print('Welcome %s %s' %(userDetails[0], userDetails[1]))
    print('You just logged in on ' + date + ' at ' + time)
    selectedOption = int(input('Please, select from the available options:\n1. Withdrawal\n2. Cash deposit\n3. Recharge\n4. Complaint\n'))
    if selectedOption == 1:
        withdraw()
    elif selectedOption == 2:
        deposit()
    elif selectedOption == 3:
        recharge()
    elif selectedOption == 4:
        complaint()
    else:
        print('Invalid option selected. Please try again')
        bankOperations(userDetails)

def withdraw():
    print('How much would you like to withdraw?')
    print('1. 1000 \n' + '2. 2000 \n' + '3. 5000 \n' + '4. 10000 \n' + '5. Other')
    selectedAmount = int(input('Please select an option: '))
    if selectedAmount == 1:
        print('Take your cash.')
    elif selectedAmount == 2:
        print('Take your cash.')
    elif selectedAmount == 3:
        print('Take your cash.')
    elif selectedAmount == 4:
        print('Take your cash.')
    elif selectedAmount == 5:
        amount = int(input('input the amount you want in multiples of 1000 \n'))
        print('Take your cash.')
                
    else:
        print('Invalid option selected. Please try again')
    
    lastOption()

def deposit():
    print('How much would you like to deposit?')
    print('1. 1000 \n' + '2. 2000 \n' + '3. 5000 \n' + '4. 10000 \n' )
    selectedDeposit = int(input('Please select an option: '))
    if selectedDeposit == 1:
        depositedCash = 1000
        print('Your current balance is: ' + str(depositedCash))
    elif selectedDeposit == 2:
        depositedCash = 2000
        print('Your current balance is: ' + str(depositedCash))
    elif selectedDeposit == 3:
        depositedCash = 5000
        print('Your current balance is: ' + str(depositedCash))
    elif selectedDeposit == 4:
        depositedCash = 10000
        print('Your current balance is: ' + str(depositedCash))
    else:
        print('invalid option selected. Please try again.')

    lastOption()

def recharge():
    print('How much would you like to recharge?')
    print('1. 100 \n' + '2. 200 \n' + '3. 500 \n' + '4. 1000 \n' + '5. Other')
    selectedAmount = int(input('Please select an option: '))
    if selectedAmount == 1:
        print('Recharge successful.')
    elif selectedAmount == 2:
        print('Recharge successful.')
    elif selectedAmount == 3:
        print('Recharge successful')
    elif selectedAmount == 4:
        print('Recharge successful')
    elif selectedAmount == 5:
        amount = int(input('input the recharge you want in multiples of 100 \n'))
        print('Recharge successful')
                
    else:
        print('Invalid option selected. Please try again') 
    
    lastOption()


def complaint():
    report = input('What issue will you like to report? \n')
    print('Thank you for contacting us.') 
    lastOption()

def generateAccount():
    return random.randrange(1111111111,9999999999)

def bankOperationsAnex():
    selectedOption = int(input('Please, select from the available options:\n1. Withdrawal\n2. Cash deposit\n3. Recharge\n4. Complaint\n'))
    if selectedOption == 1:
        withdraw()
    elif selectedOption == 2:
        deposit()
    elif selectedOption == 3:
        recharge()
    elif selectedOption == 4:
        complaint()
    else:
        print('Invalid option selected. Please try again')
        bankOperations(userDetails)

def lastOption():
    optionSelected = int(input('Press: \n1. Go Back\n2. Log out\n'))
    if optionSelected == 1:
        bankOperationsAnex()
    elif optionSelected == 2:
        quit()
    else:
        print('Invalid option selected')
        lastOption()

init()


