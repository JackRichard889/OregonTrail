from abc import abstractmethod
import pygame

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
  def render_multiline_field(self, text, entered, x, y, screen, selected):
    font = pygame.font.Font('font/font.ttf', 17)
    if entered == "" and selected:
      text += "_"
    else:
      text += entered
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 17 * i))
  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))
  def isNumber(self, number):
    try:
      int(number)
      return True
    except:
      return False