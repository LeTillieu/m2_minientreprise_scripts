import sys
import yaml

args=sys.argv

activity_name= args[1]
path='./activite/'+activity_name

config_file=open(path)

parsed_config_file=yaml.load(config_file,Loader=yaml.FullLoader)

print(parsed_config_file)

