from abc import abstractmethod

class Screen():
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    pass
  @abstractmethod
  def render(self, screen):
    pass
  @abstractmethod
  def process_input(self, key):
    pass
  def listen_for_transition(self):
    if self.next != self:
      new = self.next
      self.next = self
      return new
    else:
      return self.next
  def receive_data(self, data):
    self.data = data
  def sync_data(self):
    return self.data