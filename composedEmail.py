## Import using Library
from email.message import EmailMessage

def composingMail(mail_content):
    ## Create new Email Object
    craftedEmail = EmailMessage()
    ## Set mail content
    craftedEmail.set_content(mail_content)
    ## Set mail subject
    craftedEmail['Subject'] = 'OTP Verifying Code'
    ## Set mail sender
    craftedEmail['From'] = "Sender Email"
    ## Enter receipient email
    receipientEmail = input("Enter your email: ")
    ## Set email receipient
    craftedEmail['To'] = receipientEmail
    
    ## Return craftedEmail object to main flow
    return craftedEmail