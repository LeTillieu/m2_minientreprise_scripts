from flask import Flask
from action import Hook, Script, Wait
from threading import Thread
from sys import argv
import logging
import click
import yaml
import time

app=Flask(__name__)

#Déactivation du logging de Flask
log = logging.getLogger('werkzeug')
log.disabled = True

def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

#Configuration de Flask
@app.route('/')
def index():
  return '<h1>Hook Server running</h1>', 200

@app.route('/<string:id>')
def hook(id):
  for item in Hook.running :
    if(id == item.route):
      return '<h1>' + item.name + ' hooked </h1>', 200
  return '', 404

if __name__ == '__main__':
  kwargs = {'host': '0.0.0.0', 'port': '5443', 'threaded': True, 'use_reloader': False, 'debug': False}
  flaskThread = Thread(target=app.run, daemon=True, kwargs=kwargs,).start()

# activity_name= argv[1]
# path='./activite/'+activity_name

path='./activite/A_phishing.yml'
file=open(path)
data=yaml.load(file,Loader=yaml.FullLoader)
actions = []

for action in data['actions']:
	if(action['type']=='script'):
		actions.append(Script(action))

	elif(action['type']=='wait'):
		actions.append(Wait(action))

	elif(action['type']=='hook'):
		actions.append(Hook(action))

	else:
		raise Exception("Action must have a type")

while len(actions) > 1 :
	action = actions.pop(1)
	action.run()
