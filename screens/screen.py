from abc import abstractmethod

class Screen():
  def __init__(self):
    pass
  @abstractmethod
  def render(self):
    pass