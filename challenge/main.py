data = {}

def registration():
    username = input('please enter your username')
    password = input('enter your password')
    data[username] = password
    print(f"hi {username} your account has been created")
    return login()


def login():
    username = input('please enter your username')
    password = input('enter your password')

    if username in data.keys():
        if password == data[username]:
            print(f"welcome {username}  you are now logged in")
        else:
            print("you got a wrong password dude")
    else:
        print(f"sorry theres no username as {username} please try again or create an account")


registration()
print(data)