#! /usr/bin/python3

import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage
import os

""" for the Task8 ,I have modified my old task to send txt file and image as an attachment"""

def emil_sender(subject,body):
    gmail_user="obdphoo25@gmail.com"


    with open("password.txt") as filereader:
        gmail_password=filereader.read()

    to = ['pilvi.bichonfrise@gmail.com']
    with open('normal.jpg', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="example.jpg")
        
    filename="hard.txt"
    image_name="normal.jpg"
    img_data = open(image_name, "rb").read()
    image = MIMEImage(img_data, name = os.path.basename(image_name))
    msg = EmailMessage()
    msg.set_content("Here is Task8 hard,Ascii image and txt ")
    msg.add_attachment(open(filename,"r").read())
    msg.attach(img)
  
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to


    while True:
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
        except:
            print('cannot connect to server')
            break
        try:
            server.login(gmail_user,gmail_password)
        except:
            print('error with user name or password')
            break
        try:
            server.send_message(msg)
        except:
            print('error with sending a mail')
            break
        try:
            server.close()
        except:
            print('error with closing server connection')
            break
        break
if __name__ =="__main__":
    emil_sender("error from app with function ","hard.txt")