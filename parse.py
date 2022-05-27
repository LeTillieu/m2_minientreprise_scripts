from flask import Flask, redirect, request, render_template
from action import Hook, Script, Wait
from threading import Thread
from os import path
from sys import argv
from logging import getLogger
import click
import yaml

app=Flask(__name__)

#Déactivation du logging de Flask
log = getLogger('werkzeug')
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

@app.route('/<string:id>', methods = ['GET', 'POST'])
def hook(id):
  for item in Hook.running :
    if id == item.route:
      if item.once:
        item.stop()

      if request.method == 'POST' and item.data:
        file = request.files['file']
        file.save(f"./out/{item.data}")

      if item.action:
        item.action.target = request.remote_addr
        item.action.run()

      if display:=item.display:
        if display['type'] == 'redirect': return redirect(display['value'], 302)
        if display['type'] == 'template': return render_template(display['value'])

      return item.name, 200

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
