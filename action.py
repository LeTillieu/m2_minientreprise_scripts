class Action:
  def __init__(self, name):
    self.name = name

  def run():
    pass


class Script(Action):
  def __init__(self, name, script):
    super().__init__(name)
    self.script = script


class Wait(Action):
  def __init__(self, name, time):
    super().__init__(name)
    self.time = time


class Hook(Action):
  running = []

  def __init__(self, name, route):
    super().__init__(name)
    self.route = route
    Hook.running.append(self)

  def __del__(self):
    Hook.running.remove(self)

