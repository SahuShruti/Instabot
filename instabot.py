from email import message
from time import sleep
from getpass import getpass
from instabot import Bot
from os import remove
my_bot = Bot()
# introduction to app
print("WELCOME TO INSTABOT CLI APPLICATION")
sleep(2)
print("setting up the connection with https://www.instagram.com/",end="")
for i in range(3):
    sleep(1)
    print('.',end="")
print()
sleep(2)
print("connection established!")

# login user
username = input("username: ")
password = getpass(prompt="password: ")
my_bot.login(username=username,password=password)
#print("--LOGGED IN SUCCESSFULLY")
print(f"--{username}-logged in successfully")

while(true):
    print("choose suitable options")
    print("""1. follow user\n2.unfollow user\n3. send message user\n4.exit the app""")
    print("enter the option you choose:",end="")
    n=int(input())
    if n==1:
        user=input("enter username:")
        my_bot.follow(user)
        print(f"--{user}FOLLOWED.--")
    elif n==2:
        user=input("enter username:")
        my_bot.unfollow(user)
        print(f"--{user}UNFOLLOWED.--")
    elif n==3:
        user=input("enter username")
        message=input("message you want to send: ")
        my_bot.send_message(message,user)
        print(f"--MESSASGE SUCCESSFULLY SENT TO {user}.--")
    elif n==4:
        my_bot.logout()
        print("logging out the user",end="")
        for i in range(3):
            sleep(1)
            print('.',end="")
        print()
        sleep(2)
        print("connection ended")
        print("logged out successfully")
        break
    else:
        print("Wrong input, choose again")
        
remove('./config')