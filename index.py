

from operator import contains
from random import randint
from time import sleep
import re



 


# Login system before starting game
#Ask if has account 
# if has has no account create an account else login
# create an account 
# ask for passsword and username
# create a dictionary to keep the names




# setting up a class to take care of login funtion
class Create_account:
    def __init__(self):
        self.name = input("Input Username ")
        self.password = {"password1" :(input("Input Password")), "confirm_password1":(input("Confirm Password "))}
        while  self.password["password1"] != self.password["confirm_password1"]:
            print("Password Mismatch")
            exit()
        self.password_correct = self.password["password1"]
        return None
      
class Login:
    def __init__(self):
        self.username = input("Username ")
        self.password = input("Password ")


users_database = {"john":"123s"
    
}

ask_if_has_account = input("Do you have an account ").lower()
if ask_if_has_account == "no":
    print("Create an account")
    new_user = Create_account() 
    flag = 0
    if not re.search("[a-z]", new_user.password_correct):
        flag = 1
    elif not re.search("[A-Z]", new_user.password_correct):
        flg = 1
    elif not re.search("[!@#$%&*()+=]", new_user.password_correct):
        flag = 1
    elif len(new_user.password_correct) < 6:
        flag = 1
    if flag == 0:
        print("Account created succesfully***")
        dic = {new_user.name:new_user.password_correct}
        users_database.update(dic )
        user = Login()
        if  user.username in users_database:
                print("Logged In")
        else:
                print("Invalid username or password")


elif ask_if_has_account == "yes":
    user = Login()
    for  detail in users_database:
        if user.username in detail:
            print("Welcome {} Logged In".format(user.username))
            break           
        else:
            print("Invalid username or passwword")
            









""""

print("WELCOME TO THE WORLD OF SACRED SECRETS")
print("Seting up the platform wait........")
sleep(1)


# Checking eligibility of player
count = 0
name = str(input("Name: "))
for char in name:
    if re.search(r"[0-9-/!@#$%&*?><\"]", name):
        warning = input("Are you sure {} is your name [Enter Yes/No]? ".format(name)).lower()
        count += 1
        if count == 1:
            print("Asking for the last time")
            
        elif  warning == "no" :
            print("Type in the correct name")
            name = input("Name: ")
            break
        elif  warning == "yes": 
            print("Alright lets continue")
            break    
try:
    age = int(input("Age ")) # Age elegibility 
    while True:
        if age  <= 18:
            print("You are not eligibe to play this game, you must be 18 or above")
            break 
    
        else:
            countries = ("america,ghana,nigeria")
            count =  input("Country: ").lower() 
            for c in countries.split():
                if not count in countries:
                    print("We are sorry, Game cannot be played in your country")
                    break
                else: 
                        # welcoming of player 
                    print("Hi Mr {} please there is no highest score its yours for the taking".format(name))

                    wanna_play = input("Do you want to begin {Enter Yes/No} ").lower() # checking readiness of player
                    guesser = randint(1,10)
                    attempts = 0
                    while wanna_play == "yes":
                        try:
                            user_input = int(input("Input number between 1 and 10?: "))
                            attempts  += 1
                            if user_input == guesser:
                                print("Bravooo!! you guessed the correct answer,  the secret number is  {}".format(guesser))
                                print("It took you {} attempts".format(attempts))
                                break 
                            elif attempts == 5:
                                print("Sorry, you have tried {} times you have exhusted all your chances :-".format(attempts))
                                break
                            elif user_input >=  10:
                                 print("Input must be between 1 and 10, you typed {}.".format(user_input))
                            elif user_input > guesser:
                                    print("The secret number is lower")
                            elif user_input < guesser:
                                    print("The secret number  is  higher")        
                        except ValueError as v:
                            print("Oooops!, you typed an alpha--{}".format(v))
                    else:
                        print("Thanks for trying our app")
            break
except Exception:
    print("Invalid input, logged out")
sleep(1)       
print("Good bye")
"""




