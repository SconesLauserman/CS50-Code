    #########################################
  ##:::::::::::::::::::::::::::::::::::::::::##
'''                LIBRARYS                   '''
"""vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"""
#:::::::::::::::::::::::::::::::::::::::::::::::#
from email.mime.multipart import MIMEMultipart  # MIMEMultipart at email.meme.multipart; built-in
from email.mime.text import MIMEText            # MIMEText at email.meme.text; built-in
import ssl                                      # ssl; pip install ssl
import smtplib                                  # smtlip; pip install secure-smtplib
from random import choice                       # choice at random; built-in
import re                                       # re; built-in 
#:::::::::::::::::::::::::::::::::::::::::::::::#
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
'''               LIBRARYS                    '''
  ##:::::::::::::::::::::::::::::::::::::::::##
    #########################################


# Acceptible keycodes in the email verification code.
digits = "1234567890"


def main(reciver):

    authentication_code = GenerateRandomKey(3, list(digits)) # Generate Random key with () with length of 3 and all the digits from 1-9.

    html_code = make_html_code(authentication_code) # Make html code with () of the auth code.
    
    dictanarie_value = make_dictanarie_values(reciver, html_code) # Make the dictanarie of the neccessary value to send a email from python.

    SendMail(dictanarie_value) # Sendint the mail.

    return authentication_code # Returning the auth code.


def make_dictanarie_values(reciver, html):

    # Making the dictanrie of neccesary values to send a mail
    full_response_dictanarie = {'email_sender': 'wei987637@gmail.com', 
                                'email_reciver': reciver,
                                'email_device_password': 'yhpydizlvwjnqtrr',
                                'email_subject': 'Authentication code',
                                'email_body': html}
    return full_response_dictanarie


def make_html_code(authentication_code):
    # The html of the email.
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
<style>
    p {
        border: 10px solid black;
        width: 80%;
        height: 200px;
        font-size: 70px;
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    body {
        padding: 0;
        margin: 0;
    }
</style>
</head>
<body>
    <center>
        <p>something</p>
    </center>
</body>
</html>
    """
    
    # Returning the html splitted into 3 parts; html, auth_code, html. and then replaing the auth_code part with the real auth code.
    return html.replace(re.split("<p>|</p>", html)[1].strip(), authentication_code)


def GenerateRandomKey(length, included):
    try:
        # Making for loop the specified length, and then incrementing the output with a random key_code from the acceptable key_codes.
        output = ''
        for _ in range(length):
            output += choice(included)
        return output
    # This is very unlikely to happen.
    except Exception:
        return "Something went wrong sent from generate random key luca"


def SendMail(values):
    # Settings up the prep to send the mail; from, to, subject.
    em = MIMEMultipart()
    em['From'] = values['email_sender']
    em['To'] = values['email_reciver']
    em['Subject'] = values['email_subject']
    
    # Attaching the html code to the mail.
    html_part = MIMEText(values['email_body'], "html")    
    em.attach(html_part)
    

    # Settings the ssl context to default.
    context_default = ssl.create_default_context()

    # Sending the e-mail.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context_default) as smtp:
        
        try:
            smtp.login(values['email_sender'], values['email_device_password']) # Opening the google account to send the e-mail from.
            smtp.sendmail(values['email_sender'], values['email_reciver'], em.as_string()) # Send the mail with the reciver and the sender.
        except Exception as error:
            return print("Something went wrong trying to send the e-mail: "+error)