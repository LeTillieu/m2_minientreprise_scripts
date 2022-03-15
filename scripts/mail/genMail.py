import time
import datetime
import random
from jinja2 import Environment, FileSystemLoader
import os
import math
import unidecode
from mail.template.genCommande import genCommande,genPub


while(True):
	
	action=random.random()
	if(action<0.75):
		content,sender,subject=genCommande()

		cm="python3 mail/mail.py -f '{}' -t 'jean.dusalon@inthebox.fr' -s '{}' -c \"{}\"".format(sender,subject,content)

		os.system(cm) 

	if(action<0.3):
		dest = ["jean.dusalon@inthebox.fr", "alain.melon@inthebox.fr", "catherine.doccasion@inthebox.fr", "michel.stock@inthebox.fr", "sylvie.compta@inthebox.fr"]
		content,sender,subject=genPub()
		for d in dest:
			cm="python3 mail/mail.py -f '{}' -t '{}' -s '{}' -c \"{}\"".format(sender,d,subject,content)

			os.system(cm) 

	exit()

	if(wait>30) :
	  wait=wait-10
	time.sleep(wait)
