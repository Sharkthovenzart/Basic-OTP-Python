## Import all using library
import os

## Import function from another file
from makeOTP import randomOTP
from craftedOTP import craftingOTP
from composedEmail import composingMail
from sendingEmail import sending

def main():
    OTP = randomOTP()
    craftedOTP = craftingOTP(OTP)
    craftedEmail = composingMail(craftedOTP)
    sending(craftedEmail)
    # Verifying Phrase
    user_input = input("Enter your OTP >> ")
    if user_input == OTP:
        print("Verified !")
    else:
        print("Wrong OTP !")

if __name__ == "__main__":
    main()