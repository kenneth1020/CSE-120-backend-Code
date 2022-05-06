#import many library for the gmail Api
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
#for message send functions
from email.mime.text import MIMEText
from email import errors
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.labels']


creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('gmail', 'v1', credentials=creds)

#Sending messages by taking any email, emailSubject,and email Context
def send_message(sendToEmail, emailSubject , emailContext):
    gmail_from = 'NoReply@ISSNAF.com'
    gmail_to = sendToEmail
    gmail_subject = emailSubject
    gmail_context = emailContext
    #Creating the email 
    message = MIMEText(gmail_context)
    message['to'] = gmail_to
    message['from'] = gmail_from
    message['subject'] = gmail_subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    body ={'raw': raw}
    try:
        service.users().messages().send(userId='me', body=body).execute()
        #print("YOUR MESSAGE HAS BEEN SENT")
    except errors.MessageError as error:
        print ('An error occured: %s' %error)


#if __name__ == '__main__':
#    main()
#send_message('davenrenz@yahoo.com', 'Testing Function', 'Does it work?')   


