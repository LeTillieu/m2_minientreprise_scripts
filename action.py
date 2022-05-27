from time import sleep
from os import system, path

class Action:
  def __init__(self, action):
    self.name = action['name']
    self.desc = action['desc'] if 'desc' in action else None

  def run(self):
    pass


class Script(Action):
  def __init__(self, action):
    super().__init__(action)
    self.script = action['script']
    self.hosts = action['hosts']
    self.args = action['args']

  def run(self):
    params = ''
    if self.args:
      for param in self.args:
        params+=' -'+param['name']+' '+str(param['value'])

    for host in self.hosts:
      if host['name'] == 'target' and self.target:
        host['name'] = self.target

      if host['name'] == 'local':
        print(f'./scripts/{self.script}{param}')
        system(f'./scripts/{self.script}{param}')
      else :
        print(f"Executing {self.script} on {host['name']}")
        system(f"scp ./scripts/{self.script} {host['name']}:.")
        if path.isdir(f"./scripts/resources/{self.script}"):
          system(f"scp -r ./scripts/resources/{self.script} {host['name']}:./resources")
        system(f"ssh -fn {host['name']} 'sudo ./{self.script}{param}'")

class Wait(Action):
  def __init__(self, action):
    super().__init__(action)
    self.text = action['text']
    self.time = action['time'] if 'time' in action else None

  def run(self):
    if self.time:
      print(self.text)
      sleep(self.time)
    else :
      choice = input(self.text)


class Hook(Action):
  running = []

  def __init__(self, action):
    super().__init__(action)
    self.route = action['route']
    self.redirect = action['redirect'] if 'redirect' in action else None
    self.once = action['once'] if 'once' in action else False
    self.data = action['data'] if 'data' in action else None
    self.display = action['display'] if 'display' in action else None
    self.action = Script(action['action']) if 'action' in action else None

  def run(self):
    Hook.running.append(self)

  def stop(self):
    Hook.running.remove(self)

