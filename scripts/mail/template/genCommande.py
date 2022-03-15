from jinja2 import Environment, FileSystemLoader
import os
import random
import unidecode
from faker import Faker

def genCommande():
	data={
		'prenom':["nathan","jean-marie","etienne","françois","dominique","eloi","jean-marc","hugues","damien","rené","antoine","léo","lilian","théo","benjamin","clément"],
		'nom':["dupond","martin","bernard","dubois","petit","lefevre","bon,net"],
		'fourn':["@gmail.com","@outlook.com","@hotmail.com","@yahoo.fr"]
		}

	fourn_sender=random.choice(data['fourn'])
	name_sender=random.choice(data['prenom'])
	last_sender=random.choice(data['nom'])
	email_sender=unidecode.unidecode(name_sender)+"."+last_sender+fourn_sender

	nbr_bn=random.randint(0,11)
	nbr_bb=random.randint(0,11)

	data_html={
		'email_sender':email_sender,
		'name_sender':name_sender.capitalize(),
		'last_sender':last_sender.capitalize(),
		'nbr_bn':nbr_bn,
		'nbr_bb':nbr_bb,
		'address': Faker("fr_FR").address()
	}

	env=Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
	template=env.get_template('commande.html')
	content=template.render(data=data_html)
	return [content,email_sender,"Nouvelle Commande de Boites"]


def genPub():
	templates=os.listdir("./mail/template/templatepub")
	pub_to_send=random.choice(templates)
	name_company=pub_to_send.split('.')[0]

	email_sender="contact@"+name_company+".com"
	f=open('./mail/template/templatepub/'+pub_to_send)
	content=f.read()
	f.close()

	return [content,email_sender,"Pub "+name_company]


	























