from abc import abstractmethod

class Screen():
  def __init__(self, data: dict):
    self.data = data
    self.next = self
    self.idle = False
    pass
  @abstractmethod
  def render(self, screen) -> None:
    pass
  @abstractmethod
  def process_input(self, key: chr) -> None:
    pass
  def listen_for_transition(self) -> "Screen":
    if self.next != self:
      new = self.next
      self.next = self
      return new
    else:
      return self.next
  def receive_data(self, data: dict) -> None:
    self.data = data
  def sync_data(self) -> dict:
    return self.data