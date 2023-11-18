### Real Time Chat App With Login System That Includes Email Verification

1. **Video Demo:** [Watch the demo](https://youtu.be/1zVOE9AyhWQ)
2. **Description:** A website that allows users to send messages at any moment.


    Register/Log in:

    When you go into the website you will get prompted to either log in or register, you don't have access to any other page.
    To log in you'll have to give 5 data values FirstName, LastName, Username, Email, Password.
    TO log in you have to fill some different requirements here is them all:
    FirstName: /^[a-zA-Z]*$/,
    LastName: /^[a-zA-Z]*$/,
    Username: "Username",
    Email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
    Password: /^[^,]*$/,
    Code: /^[0-9].+$/
    This is the regexes you have to follow to complete register, the reason username don't have a regex,d
    is because you can be named anything you want, it just has to be unique.
    When you have completed the first step of register you will get a mail, or get sent back to register if you did it wrong.
    The mail is sent from a script on the server called "SendMail.py",
    this script generates a verification code and saves it in the sessions, 
    it then takes the verification code and applies it to the already made HTML code that will be sent with the mail.
    The mail then gets sent to the user, who then has to take this verification code and put it in the input field.
    If the user does this correctly then the user will be logged in, and this gets done with saving their username in the sessions.

    When you have a username saved in the sessions then you are logged in because the way the pages knows if you are logged in,
    is if you have a username saved in the sessions, and with that you can access /chat and any other page there is.
    In all we have 10 pages on the server, but only 3 are in use, that is /register, /login and /chat the others are only for show.


    Adding a friend: 

    To add a friend, you simply has to click the add friend button at the top left corner, here there is two button; Add Friend and AddGroup,
        -Only AddFriend is working while the AddGroup is under development.
    Now click the Add Friend button and then there will appear within the list of friends hierarchy, a input field
    within this give you're new and/or friend username, when you have giving it to the input field and hit Enter,
    it will run some tests to see if you're new friends username is valid, the program will reject it if it is:
    Nothing,
    If the user already exist in you're friends profile,
    If the user doesn't exist anywhere.
    The program will simply return nothing and there won't happen anything.

    If you give a valid username the program will add them to your profile and make a dedicated file to you and you're friends chat
    it will make a dedicated file in you're and their profile. which means as soon as they reload the page you are also their friend.

    Sending Messages:
    To send a message you have to be within a users chat history, to do this click their li element in the list of friends hierarchy,
    When you have clicked the li element you and you're friends Chat History will get displayed.
    Now you can go down in the input field at the bottom and within type you're message, when you have dont that you can either,
    click on the send button or you can simply hit Enter both acchive the same result.
    When you send a message it will add it in you're and their profile and has a typical response time under 1 second for your friend to see the message.


    File Structure:
    Users 
        username1 <folder>
            ChatHistory <folder>
                friendUser1 <txt>
                    username1 >:()||| This is a message i am sending to you my friend, how are you doing at the time? $)!@#%%^ <conversation>
                    friendUser1 >:()||| Hello, thanks for asking, i am doing alright, but i am kinda bored for the time, how about you? $)!@#%%^ <conversation>
                friendUser2 <txt>
                friendUser3 <txt>
                friendUser4 <txt>
                friendUser5 <txt>
            UserData.txt <txt>
        username2 <folder>
        username3 <folder>
        username4 <folder>
        username5 <folder>
        Emails.txt <txt>
    

    Verification Code/SendMail():

    When you type in all you're data to the input fields within register you will get a email to you're inputted email address, let's look into how it does this:
    
    To send the mail we have a dedicated python file names "SendMail.py" within this we have 5 functions and 119 lines of code, here is all the functions and their purpose: 


    main << The main function takes one parameter which is the e-mail the new mail should be sent to. To send a mail this is the only function you need to trigger since it is the one that connects all the function and sends the mail

    make_dicatanrie_values << The make_dictanrie_values function takes two parameters, this is receiver and html. What the function does is it makes a dictionary of the necessary values to execute a mail from the script, here we have to give; sender, receiver, device password, subject and body/content.

    make_html_code << The make_html_code, takes one parameter which is authentication_code the function itself has a variable that is the html code, this is a large set of text and therefore has a function connected to it.
    It then returns the HTML code with the new auth code placed within it, using regex.

    GenerateRandomKey << The GenerateRnadomKey function is a simple function that takes two parameters; length which tells how long the auth code should be, included which is a list of all the keys that the auth code should include, it then makes a for loop length times and then chooses a random key from the included using random.choice, and then returns the newly random generated auth code.

    SendMail << The SendMail function takes only 1 parameter values, this is giving from the make_dictanrie_values function. The send mail function sets all the values together and then with smtplib, which is a non built-in library, sends the mail to the recipient with the new auth code.

    The mail function has 4 libraries in it, here 2 of them are not built in so you have to install, these 2 are; ssl, secure-smtplib.

    
    When the main function has sent the mail it then returns the new auth code, for the flask app to use.



    Different Python Files & How They Work: 




    JavascriptCall << The JavaScript call file is a python file with some collected functions that mainly do and/or check File I/O, the JavascriptCall file has 6 functions in it, and in all there is 131 lines of code. Let's look into these different function: 


    SearchUsernames(JavascriptCall) << The SearchUsernames function simply list all the files within the current users chat history folder, and then assembles some HTML code for the page to display.

    CheckUsernameValid(JavascriptCall) << The CheckUsernameValid function list all the folders/files and checks if the giving username exists already, if it does it returns "Invalid" else; "Valid".

    CheckEmailValid(JavascriptCall) << The CheckEmailValid function opens the Emails.txt file within the Users folder, and then splits each mail from each other using this split pattern "!#$%&", it then makes a for loop thru each mail, and checks if any of the mail is equal to the giving, if so; return "Invalid" else; "Valid ".

    AddUserToFriendList(JavascriptCall) << The AddUserToFriendList function takes 2 parameters; current user, new friend. The function returns nothing if you do either:
    Give empty string as either current user or new friend,
    Give a string new friend that already exist in the current user hierarchy,
    Give a string new friend that doesn't exist anywhere in the Users folder.
    If you are to give a valid input, then it will make a file within the current users chat history and the new friend user, it then returns some new HTM code that will get displayed within the friends hierarchy.

    ReturnChatHistory(JavascriptCall) << This function get triggered when the user clicks on one of their friends, and then the function returns all the chat history between the current user, and there clicked friend, in an HTML kind format, also splitting the history into classes of; CurrentUserMessageContainer, and FriendUserMessageContainer, this helps the page to identify what to label as receiving and outgoing text.

    SendMessageToUser(JavascriptCall) << This simply opens both the friend user, and current user files with each other and then writes to both files the new message sends. The function to help organize messages ends and splitting username with messages, it then for these purpose end each message with this pattern "$)!@#%%^" and splits the username and comment with this ">:()|||".



    SaveLoginData << The save login data is a python file that has two functions in it; login, signup. The function makes sense in names, but here is a look into how they work: 


    login(SaveLoginData) << The login function first checks if the username exists, if it does then it proceeds to open the folder with that usernames name on it, and goes into the within the file "UserData.txt", which is a file giving to each user on register that holds the following data; FirstName, LastName, Username, Email, Password. The function then takes the password from the file and the given password, compares them; if they check it then signs the user in, else it simply redirects the user back to the login screen again.

    singup(SaveLoginData) << The signup function takes 5 parameters, this is them all; firstname, lastname, username, email, password. The function then makes two folders; 1 folder within the users folder named after giving username, another folder within the just made folder called "ChatHistory ''. 
    It then makes a file called "UserData.txt" where it writes all the given data in the parameters to it, it also writes the mail to "Mails.txt".







    End: This was my Final Project for CS50P, thanks for reading my README.md file!
