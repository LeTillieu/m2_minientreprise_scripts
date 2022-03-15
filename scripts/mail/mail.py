import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
import sys
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('-f',help='mail sender')
parser.add_argument('-t',help='mail reciever')
parser.add_argument('-s',help='subject of mail')
parser.add_argument('-c',help='content of mail')

args=parser.parse_args()

server = smtplib.SMTP("192.168.3.2", 25)
#server.set_debuglevel(1) # Décommenter pour activer le debug

server.ehlo()


fromaddr = args.f
toaddrs = args.t # On peut mettre autant d'adresses que l'on souhaite
sujet = args.s

message = args.c
content=MIMEText(message,'html')
MESSAGE=MIMEMultipart("alternative")
MESSAGE["subject"]=sujet
MESSAGE["To"]=toaddrs
MESSAGE["From"]=fromaddr

MESSAGE.attach(content)

try:
  
    server.sendmail(fromaddr, toaddrs,MESSAGE.as_string())
except smtplib.SMTPException as e:
    print(e)

server.quit()

