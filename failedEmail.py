from googleapiclient import discovery
import email
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import os
import sys

# This opens the authentication json file if it has been created before
store = file.Storage('tokenFileReader.json')
creds = store.get()

# If the credits don't work or don't exist, create them, and 
# store them for future use. SCOPES are the different parameters 
# we are granting our API object access to The different scopes can 
# be found here - https://developers.google.com/gmail/api/auth/scopes
SCOPES = 'https://mail.google.com/'
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)

# We create the Gmail API object
service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

def messageReader(userEmail):
    # Extract gmail messages from user's inbox
    user_id = 'me'

    # The label_ids parameter allows you to filter by labels.
    label_id_one = 'INBOX'
    label_id_two = 'UNREAD'

    # Call the Gmail API Reading email of the user's inbox that is unread
    unread_messages = service.users().messages().list(
        userId=user_id, labelIds=[label_id_one, label_id_two]).execute()

    #We get the messages list from the dictionary of if it exists
    try:
        message_list = unread_messages['messages']
    except(Exception):
        #print("No unread messages")
        return True

    # We loop through the message_list of unread emails
    for message in message_list:
        message_id = message['id'] #This gets the unique id of the message
        
        #Fetch the unique messages using the API obeject Payload and headers
        message = service.users().messages().get(userId=user_id, id=message_id).execute()  
        
        #Load the message and parse it
        payload = message['payload']
        header = payload['headers']

        #Check if the message is a failed delivery or just a successful one
        cleanUpMail = True

        #reading different part of the header
        for parts_of_header in header:
            #print(parts_of_header)
            #If the header is from, then we know it is a failed delivery
            if parts_of_header['name'] == 'X-Failed-Recipients':
                
                #We get the msg_subject from the header
                msg_subject = parts_of_header['value']

                #If the subject is X-Failed-Recipients, then we keep the email unread
                cleanUpMail = False

                #If the userEmail is in the subject, then we know it is a failed Address.
                #Return false if the userEmail is in the subject
                #Make the mail as read
                if userEmail in msg_subject:
                    #print failed message and return false. Marking the mail as read
                    #print("Failed Recipient: " + msg_subject)
                    service.users().messages().modify(userId=user_id, id=message_id, body={
                                                    'removeLabelIds': ['UNREAD']}).execute()
                    #Return false to indicate that the email is a failed delivery
                    return False
                            
        #If the mail is not a failed delivery then we can mark it as read. Cleaning the mail list for the next iteration
        if(cleanUpMail == True):
            #print "Clean Up Mail"
            service.users().messages().modify(userId=user_id, id=message_id, body={
                                                    'removeLabelIds': ['UNREAD']}).execute()
    #Return true to indicate that the email is a successful delivery
    return True