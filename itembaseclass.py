from abc import abstractmethod

class BaseItem():
  stackable_size: int
  def __init__(self):
    pass
  @abstractmethod
  def interact(self):
    pass