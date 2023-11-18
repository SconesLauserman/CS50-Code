from flask import session, request
import os


def SearchUsernames(CurrentUser):

    # List all files within the currentUsername ChatHistory dir, and then return it
    Usernames = os.listdir(f"Users/{CurrentUser}/ChatHistory")
    Output = ""
    for username in Usernames:
        Output += f"<li class='username_in_list_onclick'>{username}</li>"
    return Output


def CheckUsernameValid(username):

    # List all folders/files within the Users folder and returning if the Username search is within it then return 'Invalid' and else 'Valid'
    List_Usernames = os.listdir("Users")
    if username not in List_Usernames:
        return "Valid"
    else:
        return "Invalid"


def CheckEmailValid(email):
    try:
        
        # Open the Emails.txt file and make a for loop thru each mail splitted with this "!#$%&"
        with open("Users/Emails.txt", "r") as Emails:
            EmailsArray = Emails.read().split("!#$%&")
            for NewMail in EmailsArray:
                if NewMail == email:
                    return "Invalid"
                else:
                    return "Valid"
    except Exception:
        # This will propally happen if the File was not found
        return "Invalid"


def AddUserToFriendList(CurrentUser, NewFriend):
    try:

        if NewFriend in os.listdir(f"Users/{CurrentUser}/ChatHistory"): # Cheking if the user alredy exist.

            # Making for loop thru each user the user is alredy friends with and returning that.
            output = ''        
            for friend in os.listdir(f"Users/{CurrentUser}/ChatHistory"):
                output += f"<li class='username_in_list_onclick'>{friend}</li>"
            return output        

        else: # If the user does not exist(valid) then do the following...

            # Make a file within the new friends user dir. 
            with open(f"Users/{NewFriend}/ChatHistory/{CurrentUser}", "a") as NewUserChatData:
                NewUserChatData.write(f"")
            
            # Make a file within the current users dir.
            with open(f"Users/{CurrentUser}/ChatHistory/{NewFriend}", "a") as NewUserChatData:
                NewUserChatData.write(f"")

                # Making a for loop thru each of the current user friend list now including the new friend and displaying it.
                output = ''        
                for friend in os.listdir(f"Users/{CurrentUser}/ChatHistory"):
                    output += f"<li class='username_in_list_onclick'>{friend}</li>"
                return output
            
    except Exception: # This can only accour two times if the user is alredy friends with eachother; or if the current user sent nothing.
        # Make a for loop thru the same list as always of users, because the current user didnt give a valid username.
        output = ''        
        for friend in os.listdir(f"Users/{CurrentUser}/ChatHistory"):
            output += f"<li class='username_in_list_onclick'>{friend}</li>"
        return output
    
    
def ReturnChatHistory():
    CurrentUser = session.get("username") 
    FriendUser = request.get_data(as_text=True)
    
    friendUserString = f"{FriendUser}" 
    friendUserStringNoQuotes = friendUserString.replace('"', '') 

    try:
        # Checking if the user JavaScript want to display is there = Valid.
        if friendUserStringNoQuotes in os.listdir(f"Users/{CurrentUser}/ChatHistory"):

            # File path to the two users ChatHistory.
            file_path = f"Users/{CurrentUser}/ChatHistory/{friendUserStringNoQuotes}"
            with open(file_path, 'r') as ChatData:

                ChatDataRead = ChatData.read()

                # Each comment is splitted by this pattern "$)!@#%%^".
                ChatDataSplit = ChatDataRead.split("$)!@#%%^")
                

                # Making a for loop thru each comment sent between the two users and adding them to the HTML.
                HTML = ''
                for i in range(len(ChatDataSplit) - 1):

                    # Splitting the message into two parts; Username, Message, every message is splitted into these parts with this pattern ">:()|||".
                    Username, Message = ChatDataSplit[i].split(">:()|||")
                    if Username.strip() == CurrentUser.strip():
                        HTML += f"<div class='CurrentUserMessageContainer'><div class='CurrentUserMessageClass'><div><button>{Username}</button></div><div><p>{Message}</p></div></div></div>"
                    else: 
                        HTML += f"<div class='FriendUserMessageContainer'><div class='FriendUserMessageClass'><button>{Username}</button><div><p>{Message}</p></div></div></div>"
                return HTML
        
        else:
            return 'User does not exist'

    # This can happen because in the message file the user did not include ">:()|||",
    # It can also happen because of missing file(inlikely),
    # And lack of data giving.
    except Exception:
        return f"Something went wrong trying to display you're Chat History with {friendUserStringNoQuotes}"


def SendMessageToUser():
    NewMessage = request.get_json() # Message to send.
    CurrentUser = session.get("username")

    # Opening the ChatHistory file of the two users.

    with open(f"Users/{NewMessage['Reciver']}/ChatHistory/{CurrentUser}", 'a') as ChatData: # The reciver user messsage file
        ChatData.write(f"{CurrentUser} >:()||| {NewMessage['Message']} $)!@#%%^\n")

    with open(f"Users/{CurrentUser}/ChatHistory/{NewMessage['Reciver']}", 'a') as ChatData: # The current user message file
        ChatData.write(f" {CurrentUser} >:()||| {NewMessage['Message']} $)!@#%%^\n")

        return f"<div class='CurrentUserMessageContainer'><div class='CurrentUserMessageClass'><div><button>{CurrentUser}</button></div><div><p>{NewMessage['Message']}</p></div></div></div>"