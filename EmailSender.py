import smtplib
import getpass
import sys

def main():
    """    
    sending email from the gmail account using python
    """
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    #smtp_object = smtplib.SMTP('smtp.gmail.com',465)
    #smtp_object = smtplib.SMTP('smtp.gmail.com')

    #create the server
    smtp_object.ehlo()

    #to initiate the tls encryption
    #only if using port 587
    smtp_object.starttls()

    #to setup the email and password
    #password = getpass.getpass("Enter your password: ")
    #print(password)

    #generate an app password for gmail
    #then setup email
    email_add= getpass.getpass("Email: ")
    password = getpass.getpass("Password: ")
    smtp_object.login(email_add, password) #app password

    from_address = email_add
    to_address = email_add
    subject = input("Enter the subject: ")
    message = input("Enter the body message: ")
    msg = "Subject: "+subject+'\n'+message

    #sending the email
    smtp_object.sendmail(from_address,to_address,msg)
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))
