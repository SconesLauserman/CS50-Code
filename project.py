     ##########################################################################################################
    #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#
  ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv##
'''vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'''
'''                                             IMPORTS                                                          '''
"""::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
from flask import Flask, render_template, request, session, redirect                                             ### pip install flask
from lib import JavascriptCall                                                                                   ### own modules
from lib import SendEmail                                                                                        ### own module
from lib import SaveLoginData                                                                                    ### own module
"""::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
'''                                             IMPORTS                                                          '''
'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
  ##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^##
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
     ##########################################################################################################










  #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#
 #>::::::::::::::::::::::::::::::::::::::<#
'''             VARIABLES               '''
"""VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"""
                                        ###
app = Flask(__name__)                   ### Settign app variable to be the website.
def main():                             ###
    app.secret_key = "Hello, CS50!"     ### Settings the flask app's secret key.
    app.run()                           ### RUN APP
                                        ###
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
'''             VARIABLES               '''
 #>:::::::::::::::::::::::::::::::::::::<#
  #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#










     #######################################################################################################################################
  ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv##
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
'''                                                         PROCCES LOGIN DATA                                                                '''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
@app.route('/ProccesRegisterData', methods=['POST', 'GET'])
def proccesregisterdata(): # Made to procces the users answer to the mail sent.

    # Get all the login data, from the user.    
    FirstName = request.form.get('FirstName')
    LastName = request.form.get('LastName')
    Username = request.form.get('Username')
    Email = request.form.get('Email')
    Password = request.form.get('Password')

    
    # Turning all the login data into an dict to make easier to acces.
    LoginDataDict = {
        'FirstName': FirstName,
        'LastName': LastName,
        'Username': Username,
        'Email': Email,
        'Password': Password
    }
    # Saving the login data temp in the sessionns.
    session['data'] = LoginDataDict

    # Calling the SendMail Module to send a mail to the user specified E-mail.
    VerificationCode = SendEmail.main(Email)
    
    # Saving the randomly generated E-mail code from the Send Mail generator, in sessions.
    session['code'] = VerificationCode

    # Render the HTML 'emailvarify.html'.
    return render_template("emailverify.html")


@app.route("/SaveDataRegister", methods=['POST'])
def SaveDataRegister(): # Made to check if the user inputted, the correct varification code, and if save the user data in a new file.

    if 'username' in session: # Check if username is in, if; redirect to /chat, else; ...
        return redirect("/chat")
    else:
        # Get user verification response code.
        UserCode = request.form.get("UserCode")
        
        if session.get("code") == UserCode:
            loginDict = session.get("data") #Get session login data.

            #Sending request to own module, to sign up with the data from sessions.
            SaveLoginData.signup(loginDict['FirstName'], loginDict['LastName'], loginDict['Username'], loginDict['Email'], loginDict['Password'])
            
            session.pop('data') # Popping the data when data is saved on the database.
            return redirect("/chat")
        
        else:# If code was wrong ask user fore code again
            return redirect("/ProccesRegisterData")


@app.route("/CheckLoginData", methods=['POST'])
def CheckLoginData(): # Function to sign the user in to theire profile if theire login data, checks out.
    is_valid = SaveLoginData.login()
    if is_valid:
        return redirect("/chat")
    else:
        return redirect("/login")
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
'''                                                     PROCCES LOGIN DATA                                                                    '''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
  ##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^##
     ######################################################################################################################################










     #######################################################################################################################################
  ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv##
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
'''                                                      JavaScript CALL FUNCTIONS                                                            '''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
@app.route('/SearchUsernames', methods=['POST'])
def SearchUsernames(): 
    return JavascriptCall.SearchUsernames(session.get("username"))


@app.route("/CheckUsernameValid", methods=['POST'])
def CheckUsernameValid():
    return JavascriptCall.CheckUsernameValid(request.get_json())

@app.route("/CheckEmailValid", methods=['POST'])
def CheckEmailValid():
    return JavascriptCall.CheckEmailValid(request.get_json())
    
@app.route('/AddUserToList', methods=['POST'])
def AddUserToList():
    return JavascriptCall.AddUserToFriendList(session.get("username"), request.get_json('NewFriend'))
        

@app.route("/DisplayUserChatHistory", methods=['POST'])
def DisplayUserChatHistory():
    return JavascriptCall.ReturnChatHistory()


@app.route("/SendMessage", methods=['POST'])
def SendMessage():
    return JavascriptCall.SendMessageToUser()
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
'''                                                     JavaScript CALL FUNCTIONS                                                             '''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
  ##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^##
     ######################################################################################################################################











     #######################################################################################################################################
  ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv##
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
'''                                                         GENERAL PAGES                                                                     '''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
@app.route("/chat", methods=['POST', 'GET'])
def test():
    if 'username' in session:
        return render_template("Chat.html")
    else:
        return redirect("/register")
@app.route("/", methods=["POST", "GET"])

@app.route("/")
def index():
    if 'username' in session:
        #render the page you are currecntly working on
        return render_template("Chat.html")
    else:
        return redirect("/register")


@app.route('/register', methods=['POST', "GET"])
def register():
    if 'username' not in session:
        return render_template("Register.html")
    else:
        session.pop("username")
        return redirect("/register")


@app.route('/login', methods=['POST', "GET"])
def login():
    if 'username' not in session:
        return render_template("Login.html")
    else:
        session.pop("username")
        return redirect("/login")


@app.route('/about', methods=['POST', "GET"])
def about():
    return "This is the about page"


@app.route('/home', methods=['POST', "GET"])
def home():
    return "This is the home page"
    

@app.route('/contakt', methods=['POST', "GET"])
def contakt():
    return "This is the contact page"
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
'''                                                         GENERAL PAGES                                                                     '''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
  ##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^##
     ######################################################################################################################################










 #########################
#vvvvvvvvvvvvvvvvvvvvvvvvv#
#:::::::::::::::::::::::::#
'''        RUN APP      '''
if __name__ == "__main__":#<<<<<< IF NAME == MAIN...
    main()                #<<<<<< main() TO RUN APP
'''        RUN APP      '''
#:::::::::::::::::::::::::#
#^^^^^^^^^^^^^^^^^^^^^^^^^#
 #########################