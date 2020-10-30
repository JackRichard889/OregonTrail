from abc import *

class BaseItem():
  def __init__(self):
    pass
  @abstractmethod
  def interact(self):
    pass