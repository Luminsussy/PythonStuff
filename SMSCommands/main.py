import imaplib, email, os

# Function to get email content part i.e its body
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

# Function to search for a key value pair 
def search(key, value, con): 
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
 
    return msgs

user = ''
password = ''
imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select('Inbox') #Checks for emails under this label

allowed = ['3478633063']

#Meant to be run on linux server
while True:

    #Define commands to look for
    if msg == "":
        #Do something
        #os.system('echo "hi"')
    elif msg == "":
        
        
