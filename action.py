from time import sleep
from subprocess import Popen, PIPE
from os import system, path
import sys

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
    self.scheduler = action['scheduler'] if 'scheduler' in action else False
    self.args = action['args'] if 'args' in action else None

  def run(self):
    params = ''
    if self.args:
      for param in self.args:
        params+=' -'+param['name']+' '+str(param['value'])

    for host in self.hosts:
      if host['name'] == 'target' and self.target:
        host['name'] = self.target

      if host['name'] == 'local':
        #print(f'./scripts/{self.script}{params}')
        Popen([f'./scripts/{self.script}', params])

      else :
        print(f"Executing {self.script} on {host['name']}")
        sendOverSSH(f"./scripts/{self.script}", f"{host['name']}:.")

        if path.isdir(f"./scripts/resources/{self.script}"):
          sendOverSSH(f"./scripts/resources/{self.script}", f"{host['name']}:./resources")

        if self.scheduler :
          sendOverSSH(f"./scripts/scheduler.ps1", host['name'])
          runOverSSH(host['name'], f"./scheduler.ps1 -script './{self.script}{params}' -taskName '{self.name}' ")
        else :
          runOverSSH(host['name'], f"./{self.script}{params}")

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
      sys.stdout.write("\033[F")
      sys.stdout.write("\033[K")


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


class ScriptError(Exception) :
  pass

class SendScriptError(ScriptError):
  def __init__(self, message):
    self.message = message

class RunScriptError(ScriptError):
  def __init__(self, message):
    self.message = message


def sendOverSSH(file, target) :
  cmd = ['scp', file, target]
  if path.isdir(file) :
    cmd.insert(1, '-r')

  process = Popen(cmd, stderr=PIPE, stdout=PIPE)
  send_stderr, send_stdout = process.communicate()

  if send_stderr[0] :
    raise SendScriptError('Error went sending file')

def runOverSSH(target, command) :
  cmd = ['ssh', '-fn', target, command]

  process = Popen(cmd, stderr=PIPE, stdout=PIPE)
  run_stderr , run_stdout = process.communicate()

  if run_stderr[0] :
    raise RunScriptError('Error went running script')