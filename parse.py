from flask import Flask, redirect, request, render_template
from action import Hook, Script, Wait
from threading import Thread
from os import path
from sys import argv
import flask.cli
import logging.config
import yaml

app=Flask(__name__)

#Déactivation du logging de Flask
flask.cli.show_server_banner = lambda *args: None
logging.getLogger("werkzeug").disabled = True

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

# Lancement de Flask dans un Thread dédié
if __name__ == '__main__':
  kwargs = {'host': '0.0.0.0', 'port': '5443', 'debug': False}
  flaskThread = Thread(target=app.run, daemon=True, kwargs=kwargs)
  flaskThread.start()

# activity_name= argv[1]
file_name= 'A_phishing.yml'
path='./activite/'+file_name
file=open(path)
activite=yaml.load(file,Loader=yaml.FullLoader)
file.close()

actions = []

for action in activite['actions']:
  if(action['type']=='script'):
    actions.append(Script(action))

  elif(action['type']=='wait'):
    actions.append(Wait(action))

  elif(action['type']=='hook'):
    actions.append(Hook(action))

  else:
    raise Exception("Action must have a type")

while len(actions) > 0 :
  action = actions.pop(0)
  action.run()
