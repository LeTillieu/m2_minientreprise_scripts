import time

class Action:
  def __init__(self, action):
    self.name = action['name']

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
        params+='-'+param['name']+' '+str(param['value'])+' '

    for host in self.hosts:
      if host['name'] == 'local':
        print(f'./scripts/{self.script} {param}')
      else :
        print(f'{host.name} : ./scripts/{self.script} {param}')

class Wait(Action):
  def __init__(self, action):
    super().__init__(action)
    self.text = action['text']
    self.time = action['time'] if 'time' in action else None

  def run(self):
    if self.time:
      print(self.text)
      time.sleep(self.time)
    else :
      choice = input(self.text)


class Hook(Action):
  running = []

  def __init__(self, action):
    super().__init__(action)
    self.route = action['route']

  def run(self):
    Hook.running.append(self)

  def __del__(self):
    Hook.running.remove(self)

