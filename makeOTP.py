## Import all using library
import math as mt
import random as rd

def randomOTP():
    ## Using to random OTP
    digits_set = "1234567890"
    ## Storing OTP from random 
    OTP = ""
    ## Random Process
    for i in range(8):
        OTP += digits_set[mt.floor(rd.random()*10)]

    ## OTP text to send to user
    ## OTP_text = OTP + " is your code for verifying your identity for this app."

    ## Return OTP text to main flow
    return OTP