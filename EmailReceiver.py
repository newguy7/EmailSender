import imaplib
import getpass
import email
import sys

def main():
    """    
    checking/viewing received email from python
    """
    M = imaplib.IMAP4_SSL('imap.gmail.com')

    # grab our password and email
    email_add = getpass.getpass("Email: ")
    # app password for gmail user
    password = getpass.getpass("Password: ")

    #connect to the server
    M.login(email_add,password)

    #this shows everything we can check from our email
    M.list()
    
    #selecting the inbox
    M.select("inbox")

    #search inbox using the subject
    typ, data = M.search(None, 'SUBJECT "test_zebra"')
    #print(typ)

    #other option to search in the inbox
    #typ, data = M.search(None, 'BEFORE 23-May-2023')
    #typ, data = M.search(None, 'FROM user@example.com')
    
    email_id = data[0]
    result,email_id = M.fetch(email_id, '(RFC822)')

    #print(email_id) 
    #to grb the actual message itself
    raw_email = email_id[0][1]
    raw_email_string = raw_email.decode('utf-8')

    #to grab the actual email from the string
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        # if some link is expected in the email, use text/html
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True)
            print(body)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
