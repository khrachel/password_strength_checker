# password strength checker
# learning python

import string
import getpass #hides password

def main():
    print("Welcome to the password strength checker. It will check if your password has: 10+ characters, an uppercase letter, a lowercase letter, a number, and a special character. Here are some tips for password safety: the longer, the better, do not use personal details like your birthday or your dog's name, store your passwords in a safe space like a password manager. Do not share passwords with anyone!!")
    
    
    while True:
        password = getpass.getpass("Please enter a password: ")

        score = 0

        if len(password) >= 10:
            score += 1
        
        if any(char in string.ascii_uppercase for char in password):
            score += 1

        if any(char in string.ascii_lowercase for char in password):
            score += 1

        if any(char in string.digits for char in password):
            score += 1

        if any(char in string.punctuation for char in password):
            score += 1
        
        if score == 0:
            print("It's a surprise you haven't been hacked yet. Please change your password immediately.")
        
        elif score == 1:
            print("You have scored 1 point. Your password is weak. Please make sure to create a strong password.")

        elif score == 2:
            print("You have scored 2 points. Your password is getting there, but weak. Please make sure to create a strong password.")

        elif score == 3:
            print("You have scored 3 points. Your password is medium strong. Please make sure to create a stronger password.")

        elif score == 4:
            print("You have scored 4 points. Your password is strong, but it could be stronger. Please create a stronger password.")

        else:
            print("You have scored 5 points. Congratulations on having a strong password. To make it even stronger, please create a longer password.")

        repeat = input("\nWould you like to check another password? (yes/no): ")
        if repeat.lower() == "no":
                print("Thanks for using this! This was created as part of my journey of learning code. Anthropic's Claude assisted in creating this script. :)")
                break


main()


              
        
    
