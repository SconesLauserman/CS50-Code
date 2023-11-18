import os
from flask import session, request 


def signup(firstname, lastname, username, email, password):

    # Make the base dir, ChatHistory dir
    os.mkdir(f"Users/{username}")
    os.mkdir(f"Users/{username}/ChatHistory")

    try:
        
        with open(f"Users/{username}/UserData.txt", "a") as UserData: # Opening the base current user data.txt file.
            UserData.write(f'{firstname}, {lastname}, {username}, {email}, {password}\n')
        with open("Users/Emails.txt", "a") as Emails:
            Emails.write(f"{email}!#$%&")
        session['username'] = username # Signing the user in in the sessions.

    #This is unlikely to happen.
    except Exception:
        return "Somehthing went wrong this error happend from the sign up function in the file FileIO"


def login():
    # Get user sign in data; Username, Password.
    username = request.form.get("Username")
    password = request.form.get("Password")
    
    try: # Trying to sign in, because of sensitive data.

        with open(f"Users/{username}/UserData.txt", 'r') as userData: # Opening the user the users username Folder, with the UserData.txt file within.
            
            data = userData.read()
            if password == data.split(",")[-1].strip(): # Checking if the username matches with password. 
                
                session['username'] = username # Signing the user in.
                return True
            else:
                return False
    except FileNotFoundError: # If username does not exist run...
        return False
    except Exception: # This will run if something is wrong with my system.
        return False