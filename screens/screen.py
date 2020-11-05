from abc import abstractmethod

class Screen():
  def __init__(self, data):
    self.data = data
    pass
  @abstractmethod
  def render(self, screen):
    pass
  @abstractmethod
  def process_input(self, key):
    pass