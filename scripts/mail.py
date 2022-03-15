import smtplib
from email.utils import formatdate
server = smtplib.SMTP("192.168.3.2", 25)
server.set_debuglevel(1) # Décommenter pour activer le debug
#server.connect("192.168.3.2", 587)
# (220, 'toto ESMTP Postfix') # Réponse du serveur
server.ehlo()
#server.starttls()

#server.login('alain.melon@inthebox.fr', 'lemeloncdelicieux')
# (250, 'toto\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nSTARTTLS\nENHANCEDSTATUSCODES\n8BITMIME\nDSN') # Réponse du serveur
fromaddr = 'michel.sardou@gmail.com '
toaddrs = ['jean.dusalon@inthebox.fr'] # On peut mettre autant d'adresses que l'on souhaite
sujet = "Un Mail avec Python"
message = u"""\
Velit morbi ultrices magna integer.
Metus netus nascetur amet cum viverra ve cum.
Curae fusce condimentum interdum felis sit risus.
Proin class condimentum praesent hendrer
it donec odio facilisi sit.
Etiam massa tempus scelerisque curae habitasse vestibulum arcu metus iaculis hac.
"""
msg = """\
From: %s\r\n\
To: %s\r\n\
Subject: %s\r\n\
Date: %s\r\n\
\r\n\
%s
""" % (fromaddr, ", ".join(toaddrs), sujet, formatdate(localtime=True), message)
try:
    server.sendmail(fromaddr, toaddrs, msg)
except smtplib.SMTPException as e:
    print(e)
# {} # Réponse du serveur
server.quit()
# (221, '2.0.0 Bye') # Réponse du serveur