## Import using Library
import smtplib as smtp

def sending(craftedEmail):
    server = smtp.SMTP('smtp.gmail.com', 587)
    ## Preparing TLS connection
    server.starttls()
    ## Login as sender
    server.login("Sender Email", "Google App Code")
    ## Sending Email
    server.send_message(craftedEmail)
    ## Closing Connection
    server.quit()
    
    print("Sending successfully, please check your email...")
    return 
