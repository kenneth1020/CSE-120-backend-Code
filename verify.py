import base64
import binascii
import os
from secrets import token_bytes

#Creating a random token for user confirm
def tokenGenerate():
    tok = binascii.hexlify(os.urandom(32)).decode() 
    return tok 

#Creating a random token for url temporary
def token_urlSafe():
    tok = token_bytes(16)
    return base64.urlsafe_b64encode(tok).rstrip(b'=').decode('ascii')


