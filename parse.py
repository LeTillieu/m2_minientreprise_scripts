from re import S
import sys
import yaml
import time
import os

def script_module(action):

	action_name=action["name"]
	script_name=action['script']
	hosts=action['hosts']
	script_args=action['args']
	params=""

	if(script_args):
		for param in script_args:
			params+='-'+param['name']+' '+str(param['value'])+' '
	else:
		print(f"Nom de script manquant de le fichier de configuration pour l'action : {action_name}",action_name)
		return -1

	for host in hosts:
		try :
			if host['name']=='local':
				print(f'./scripts/{script_name} {params}')
				#os.system(f'./scripts/{script_name} {params}')
			else :
				##get all the
				print("else")

		except Exception as ex :
			print(ex)
			return -1

	return 1


def wait_module(action):

  name=action['name']
  wait_time=action['time']
  input_msg=action['input']
  text=action['text']

  if (wait_time):
    print(text)
    time.sleep(wait_time)

  if (input_msg):
    for interaction in input_msg:
      input(interaction["name"])

  return 1


def hook_module(action):
	print("un hook a été lance")
	return 1


args=sys.argv

activity_name= args[1]
path='./activite/'+activity_name

config_file=open(path)

parsed_config_file=yaml.load(config_file,Loader=yaml.FullLoader)

actions = parsed_config_file['actions']

for action in actions:

	if(action['type']=='script'):
		script_module(action)

	elif(action['type']=='wait'):
		wait_module(action)

	elif(action['type']=='hook'):
		hook_module(action)

	else:
		raise Exception("Action must have a type")


