## Program
This is Kenneth Tran branch code. I am the backend logic for ISSNAF. What have I provide for our project. We have three functions Sending Email, Failed Email, and Email Verification  

## Description
The purpose of these three codes is to provide the backend logic that will help ISSNAF with their membership form. 
Informing users using their email in the database or forms. Helping verify the user email. Informing the Admin if the user 
email has issues example bouncing, proxy, or no domain. 

***Sending Email*** function is a simple reference and import calling the send_message() in any python code. Taking in 
three string inputs (Email, Subject, Context).
```
from SendMessage import send_message
send_message(Email, Subject, Context)
``` 

***Note:***

> The sending email function only works if the Gmail API is properly set up. Please refer to the documentation of 
"Google API set up instruction" will be provided. 
**https://docs.google.com/document/d/1nZVLCFyLyJbgvHLHtHo2dH9yhZiczmnajjzF_5kmlL8/edit?usp=sharing**

***Email Verification*** is a simple baseline design to help generate a secret token that creates a unique URL for the user to 
confirm their email. If the said email is not confirmed within the given time limit. The token and link will expire. If the 
user clicks the link in time then the system will display the token working.

***Note:*** 

>The function is basic and incomplete with my skills. I have only created a test system that intakes one input email. 
Then send the user email two messages. One is for the primary confirmation link and the second one is the secondary email confirmation link.
The two links are both unique and different. 

>The Email Verification also hasn't been connected to the front page and the database. The comments of the code allow 
my teammate read my code and the task needed for the integration of the email verification

***Failed Email*** is a function that will be called to search for the email and if the email has no address. The error in mailing is display in the system Gmail. What this code does is read into system gmail. Checking for any failed reciepient of a specific email. The function will return a false boolean. Using that we can flag the email as not a valid email. 

***Note:*** 

>The function will need credentials.json to work. Please refer to the Gmail API setup if you don't have the credentials created yet. 

>When running the function it will create a tokenFileReader.json. As the ID to use your gmail to search for the error send back by Gmail API. And making email that were not failed email will be make as read. Cleaning up the inbox.

```
#terminal need install
pip3 install --upgrade oauth2client 
#code
from failedEmail import messageReader
sleep(60)
trueOrFalse = messageReader(Email)
```
***Note:*** 
> The input of messageReader is a string of the sent email. The email needed to be sent first then check. 

> Called sleep to slow down the system. **Why? What reason we need to sleep?** Emails are never instantly sent. Sometime it will take a few second for the email to be sent. With gmail api returning an error. Sleep provide time for the email to be sent.

> messageReader will return a false or true statement. Make sure you catch that boolean and use that information to handle the boolean statement

## Files
`credentials.json` A file containing the OAuth 2.0 Client IDs that connect to the Google Cloud Platform. This
json is specially made for my team. 

***Note:***

>This credentials.json only works for my team and me. Any other user can't use my credentials and needs to generate
their credentials.json. Please refer to the document "Google API set up instruction"

`SendMessage.py` A python code containing the function that will send an email to the user by using the Google Mail API. 

`Testingfunctions.py` A test python code calling the function and testing them for any error on importing and 
reference on the function 

`setupGoogle.py` A GitHub code provide by google. The purpose is to set up the Gmail API by generating the user their 
token.json that will act as the user ID. 

***Note:***

> This code requires your credentials.json. If you don't have this json please refer to the document
"Google API set up instruction"

> The token has an expiration date. It will expire at a certain time.

> Which means needing to delete the old token,json, and generate a new one. 

`verify.py` is a simple verify code that only generates tokens. Its purpose was to test and study token generating

`verifyFinal.py` A python flask code that generates a website that will take in one email. After taking the user email,
two tokens generate and create two unique confirmation links that are sent to that one email using `SendMessage.py`.
User when clicking Primary or Secondary link. 

***What will happen***

If the link expires then the user will be redirected to a page displaying "Sorry, the confirmation link you have clicked has expired." 

When the user clicks, the Secondary Email Verification link they get redirected to a page that says "Secondary Email has been verify." 

If they click on the Primary Email verify link they will get redirected to a page that says "The token works."

***Note:***

> This is a basic function in doing the email verify function. Doing tasks of generating two tokens, creating two unique URL links, sending links to a user email, the timestamp when the link has been clicked and checking if the link expires or not.

> Code is needed to implement into the front end and connected to the database. 

`failedEmail.py` checks through the sender email inbox. Checking for specific email error looking for failed recipient of the matching email. If the email has failed to send by "Address not found". The code will return a false boolean. In which we can flag the email as not valid and display it in the frontend.

## Authors and acknowledgment
Special thanks to my teammates in this project for helping do the frontend, database, and backend with me.
Creating this whole project and communicating with me. Our project would not be complete without their help 
and contribution. My team implement and called the backend code then intergrate into the main code.

***Rahul*** helping me with the formatting in the time stamps for the verification function. He's also the backend engineer for ISSNAF. 

***Aman*** and ***Ryan*** for implementation of my code into the main function. They are the frontend engineer for ISSNAF

***Preethi*** for helping connect the database and to implement the missing piece to my code in the main branch. She's the database engineer for ISSNAF

Thanks to Google for the Gmail API 

A youtube channel Pretty Printed https://www.youtube.com/watch?v=vF9n248M1yk 
for the tutorial on "Using Flask-Mail to Send Email Confirmation Links"

A youtube channel Brandon Jacobson https://www.youtube.com/watch?v=STwFOYwFz4o
for the tutorial on "Python Gmail API Send Messages | #73 (Gmail API #4)"

Article on checker bounce by Raunak Daga
https://raunakdaga.medium.com/how-to-check-for-bounce-backed-emails-in-python-3-7-6ab0c297f81c
