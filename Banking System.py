
# In this program, i implemented an online banking system.  Users can sign-up with the system, log in to the  system,
#  change their password, and delete their account.  They can also update their bank account balance and transfer money to another user’s bank account.
# User information will be imported from the “users.txt” file and account information will be imported from the “bank.txt” file. After importing, 
# the information from each file is stored in the dictionary user_accounts and bank respectively.
# Each function has been defined. See the docstring in each function for instructions on what the function is supposed to do.

def import_and_create_bank(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    Every line in the file should be in the following format:
        key: value
    The key is a user's name and the value is an amount to update the user's bank account with.  The value should be a
    number, however, it is possible that there is no value or that the value is an invalid number.

    These are the steps i implemented:

    - Created an empty bank dictionary.
    - Read in the file.
    - Added keys and values to the dictionary from the contents of the file.
    - If the key did not exist in the dictionary, created a new key:value pair.
    - If the key did not exist in the dictionary, incremented its value with the amount.
    - Some cases that i handled:
    -- When the value was missing or invalid i ignored that line and did not update the dictionary.
    -- When the line was completely blank i ignore that line and did not update the dictionary.
    -- When there was whitespace at the beginning or end of a line and/or between the name and value on a line thye were trimmed.
    - Returned the bank dictionary from this function.

    After processing every line in the file, the dictionary will look like this:
    bank = {"Brandon": 115.5, "Patrick": 18.9, "Sarah": 827.43, "Jack": 45.0, "James": 128.87}
    '''

    bank = {}

    # opens the file in read mode
    f = open(filename, 'r')
    #reads each line of the file
    lines = f.readlines()
    #iterates over each line
    for line in lines:
        
        #strips the white space at the begining and end of each line
        list = line.strip().split(":")
        #skips line if it doesn't contain name and deposit amount
        if len(list)<=1:
            continue
            #gets the key(name) and value(deposit amount) from the line
            #strips the whitespace from the beginning of each key and value
        key = list[0].strip()
        value = list[1].strip()
        #checks if deposit amount is correct
        try:
            #trys to cast value(deposit amount) to numeric
            value = float(value)
            bank[key] = bank.get(key,0) + value 
        
        except:
            #skips the line that contains non-numeric deposit number
            continue
            
    f.close()
    print(bank)
    
    return bank


def signup(user_accounts, log_in, username, password):
    '''
    This function allows users to sign up.
    If both username and password meet the requirements:
    - Updates the username and the corresponding password in the user_accounts dictionary.
    - Updates the log_in dictionary, setting the value to False.
    - Returns True.

    If the username and password fail to meet any one of the following requirements, returns False.
    - The username already exists in the user_accounts.
    - The password must be at least 8 characters.
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number.
    - The username & password cannot be the same.
    '''
    
    def valid(password):
        #This function validates the password according to the criteria mentioned above.

        #Initialized flags that turn on when meeting the password requirments
        isDigit = False
        isUcase = False
        isLcase = False
        
        if len(password) < 8:
            return False
        else:
            for i in password:
                if i.isdigit():
                    isDigit = True
                elif i.isupper():
                    isUcase = True
                elif i.islower():
                    isLcase = True
                else:
                    continue
            #if all flags are True then the password is valid, otherwise its not valid.
            if isDigit == True and isUcase == True and isLcase == True:
                return True
            else:
                return False
    #Checks if username and password are valid to create the account and initialize its log-in status    
    if (username != password) and (username not in user_accounts) and valid(password):
        user_accounts[username] = password
        log_in[username] = False
        return True
    else:
        return False
    
def import_and_create_accounts(filename):
    '''
    This function is used to create a user accounts dictionary and another login dictionary.  The given argument is the filename to load.
    Every line in the file should be in the following format:
      username - password
    The key is a username and the value is a password.  If the username and password fulfills the requirements,
    they are added into the user accounts dictionary.

    For the login dictionary, the key is the username, and its value indicates whether the user is logged in, or not.
    Initially, all users are not logged in.

    These are the steps i implemented:
    - Created an empty user accounts dictionary and an empty login dictionary.
    - Read in the file.
    - If the username and password fulfills the requirements, they were added  into the user accounts dictionary, and the login dictionary was updated.
    - Some cases that i handled:
    -- When the password was missing i ignored that line and did not update the dictionaries.
    -- Trimmed any whitespace at the beginning or end of a line and/or between the name and password on a line.
    - Returned both the user accounts dictionary and login dictionary from this function.
    '''

    user_accounts = {}
    log_in = {}

    f = open(filename,'r')
    
    #read each line
    lines = f.readlines()
    
    #iterate over each line
    for line in lines:
        #stripping the whitespace and splitting at the "-"
        list = line.strip().split("-")
        #if the username or password are missing the line is skipped
        if len(list)<=1:
            continue
        #stripping the whitespace that was between the username and password
        #checking if the username and password are both valid to create an account
        if signup(user_accounts,log_in,list[0].strip(),list[1].strip()):
            user_accounts[list[0]] = list[1]
            log_in[list[0]] = False

    return user_accounts,log_in


def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    The user_accounts dictionary stores the username and associated password.
    The log_in dictionary stores the username and associated log-in status.

    If the username does not exist in user_accounts or the password is incorrect:
    - Returns False.
    Otherwise:
    - Updates the user's log-in status in the log_in dictionary, setting the value to True.
    - Returns True.
    '''
    if (username not in user_accounts) or (user_accounts[username] != password):
        return False
    else:
        log_in[username] = True
        return True
    
def update(bank, log_in, username, amount):
    '''
    In this function, you will try to update the given user's bank account with the given amount.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to update with, and can either be positive or negative.

    To update the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    Return True if the user's account was updated.
    '''

    #case if there is a new user (however has to be logged in)
    #check if amount given by user is negative otherwise creates new bank account containing that amount
    if username not in bank:
        if amount<0:
            return False
        else:
            if (log_in[username]== True):
                bank[username] = amount
                return True
            else:
                return False
    #case if user is in the bank (still has to be logged in)
    else:
        #check if amount withdrawn leads to negative balance
        new_amount = bank[username]+amount
        if (new_amount <0):
            return False
        else:
            if (log_in[username]== True):
                bank[username] = new_amount
                return True
            else:
                return False
    
def transfer(bank, log_in, userA, userB, amount):
    '''
    This function attempts to make a transfer between two user accounts.
    Reminder:
        -bank is a dictionary where the key is the username and the value is the user's account balance.
        -log_in is a dictionary where the key is the username and the value is the user's log-in status.
        -amount is the amount to be transferred between user accounts (userA and userB). amount is always positive.

    These are the steps i implemented:
    - Deducted the given amount from userA and add it to userB, which makes a transfer.
    - Some cases that i handled:
      - userA must be in the bank and his/her log-in status in log_in must be True.
      - userB must be in log_in, regardless of log-in status however userB can be absent in the bank.
      - No user can have a negative amount in their account. He/she must have a positive or zero balance.
    
    Return True if a transfer is made.
    '''

    #check the requirments of making a transfer as mentioned above
    if (userB not in log_in) or (userA not in bank) or (log_in[userA]==False) :
        return False
    #case where account requirments are met
    else:
        #check if amount withdrawn leads to a negative balance
        check = bank[userA]-amount
        if check <0 :
            return False
        else:
            #case if recieving user is not in bank
            if userB not in bank:
                bank[userB] = amount
                bank[userA] -= amount
                return True
            #case if recieving user is in bank
            else:
                bank[userA] -= amount
                bank[userB] += amount
                return True

def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.

    If all of the following requirements are met, changes the password and returns True. Otherwise, returns False.
    - The username exists in the user_accounts.
    - The user is logged in (the username is associated with the value True in the log_in dictionary)
    - The old_password is the user's current password.
    - The new_password should be different from the old one.
    - The new_password fulfills the requirement in signup.
    '''
    def valid(password):
        
        isDigit = False
        isUcase = False
        isLcase = False
        
        if len(password) < 8:
            return False
        else:
            for i in password:
                if i.isdigit():
                    isDigit = True
                elif i.isupper():
                    isUcase = True
                elif i.islower():
                    isLcase = True
                else:
                    continue
            if isDigit == True and isUcase == True and isLcase == True:
                return True
            else:
                return False
    
    if (username in user_accounts) and (log_in[username] == True):
        if (old_password == user_accounts[username]) and (old_password != new_password) and (valid(new_password)):
            user_accounts[username] = new_password
            return True
        else: 
            return False
    

def delete_account(user_accounts, log_in, bank, username, password):
    '''
    Completely deletes the user from the online banking system.
    If the user exists in the user_accounts dictionary and the password is correct, and the user 
    is logged in (the username is associated with the value True in the log_in dictionary):
    - Deletes the user from the user_accounts dictionary, the log_in dictionary, and the bank dictionary.
    - Returns True.
    Otherwise:
    - Returns False.
    '''

    if (username in user_accounts) and (log_in[username] == True) and (user_accounts[username] == password):
        del user_accounts[username]
        del log_in[username]
        del bank[username]
        return True
    else:
        return False
    
def main():
 
    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            login(user_accounts, log_in, username, password)
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()
