# Calling libary from python
from tokenize import Token
from click import confirm
from flask import Flask, request, url_for
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
import datetime;
# Importing SendMessage.py to use the google api
from SendMessage import send_message

app = Flask(__name__)

# The secret key for token. This is using two different tokens
s = URLSafeTimedSerializer('ISSNAFSecretKeyPrimaryEmail')
s2 = URLSafeTimedSerializer('ISSNAFSecretKeySecondaryEmail')

# The request page example
# Need implement the code to recieve two email
# Sending two email 
# 1. Primary email
# 2. Secondary
# Each having their own special token 
@app.route('/',methods =['GET','POST'])
def index():        
        # This is the sample email submit button where the user type in their email
        # Request method gets email and import as string email
        if request.method =='GET':
            #this only takes in one input 'PrimaryEmail'
            return '<form action="/" method="POST"><input name="PrimaryEmail"><input type ="submit"></form>'
        
        # The creating the strings that will hold the email and called email from the form
        PrimaryEmail = request.form['PrimaryEmail']
        SecondaryEmail = request.form['PrimaryEmail'] # This is the secondary email
        
        # The tokenG is generating a token for the emails
        tokenPrimary = s.dumps(PrimaryEmail, salt='email-confirmPrimary')
        tokenSecondary = s2.dumps(SecondaryEmail, salt='email-confirmSecondary')
        
        #Creating the confirmation link with the token
        linkPrimary = url_for('confirm_emailPrimary', token=tokenPrimary, _external =True)
        linkSecondary = url_for('confirm_emailSecondary', token=tokenSecondary, _external =True)
        
        #Generating message for the user
        msgPrimary = 'Your link is {}'.format(linkPrimary)
        msgSecondary = 'Your link is {}'.format(linkSecondary)

        #Sending email using email, Subject, and Context
        send_message(PrimaryEmail, 'Confirm Primary Email', msgPrimary)
        send_message(SecondaryEmail, 'Confirm Secondary Email', msgSecondary)

        #Message letting the user know that message been sent
        return '<h1>Message has been sent to your mailbox. You have an hour to validate your primary email and secondary. Please verify primary before proceeding.</h1>'

#token website 
#/confirm_emailPrimary/ Need to be connected to registration confirm.
@app.route('/confirm_emailPrimary/<token>')
def confirm_emailPrimary(token):
    try:
        #read the token see if it has expire
        #email = s.loads(token, salt ='email-confirm', max_age=3600)
        PrimaryEmail = s.loads(token, salt ='email-confirmPrimary', max_age=3600)
        primaryConfirm = PrimaryEmail
    #If the token has expire display Error link to the user
    except SignatureExpired:
        #if token has expire display error message
        return '<h1>Sorry, the confirmation link you have click has expire.</h1>'    
    #Make email valid in database
    #primaryConfirm = 'Primary Confirm'
    primaryConfirmDate = datetime.datetime.now()
    #==========================================================
    #instead of printing put into database
    print(primaryConfirmDate)
    print(primaryConfirm)
    #When primary is confirm return user to membership form
    return '<h1> The token works</h1>'

#token website 
#/confirm_emailSecondary/ Need to be connected to registration confirm.
@app.route('/confirm_emailSecondary/<token>')
def confirm_emailSecondary(token):
    try:
        #read the token see if it has expire
        #email = s.loads(token, salt ='email-confirm', max_age=3600)
        SecondaryEmail = s2.loads(token, salt ='email-confirmSecondary', max_age=3600)
        secondaryConfirm = SecondaryEmail
    #If the token has expire display Error link to the user
    except SignatureExpired:
        return '<h1>Sorry, the confirmation link you have click has expire.</h1>'
    #If the token hasn't expire and was click
    #Make email valid in database
    secondaryConfirm = 'Secondary confirm'
    secondaryConfirmDate = datetime.datetime.now()
    #==========================================================
    #instead of printing put into database
    print(secondaryConfirmDate)
    print(secondaryConfirm)
    #secondary is confirm return to verify 
    return '<h1> Secondary Email has been verify</h1>'

#Run the app
if __name__ == '__main__':
    app.run(debug=True)