import sys
import yaml
import os
			
def script_module(action):

	script_name=action['script']
	hosts=action['hosts']
	params=''
	if(action['params']):
		for param in action['params']:
			params+='-'+param['name']+' '+str(param['value'])+' '
					
	for host in hosts:
		if host['name']=='local':
			print(f'./scripts/{script_name} {params}')
			#os.system(f'./scripts/{script_name} {params}')
	
	return 1

def hook_module(action):
	print("un hook a été lance")
	return 1

def ask_module(action):
	print("un ask a été lance")
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
	
	elif(action['type']=='ask'):				
		ask_module(action)
			
	elif(action['type']=='hook'):		
		hook_module(action)
	
	else:
		raise Exception("Action must have a type")

	
