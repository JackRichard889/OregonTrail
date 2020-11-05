from screens.screen import Screen
from screens.name_selector_screen import NameSelectorScreen
import pygame
import util


class SelectorScreen(Screen):
  def __init__(self, data):
    self.data = data
    print("Selector screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 29)
    title = font.render('The Oregon Trail', True, WHITE)
    self.render_multiline(
            "Many types of people made\nthe trip to Oregon.\n\n\nYou may:\n\n\n  1. Be a banker from\nBoston\n  2. Be a carpenter from\nOhio\n  3. Be a farmer from\nIllinois\n\n\nWhat is your choice? _",
            35, 120, screen)
    screen.blit(title, (24, 40))

  def process_input(self, key):
    if util.is_letter(key):
      charKey = str(chr(key))
      try:
        if int(charKey) < 4 and int(charKey) > 0:
          self.data["occupation"] = int(charKey)
          return NameSelectorScreen(self.data)
        else:
          return self
      except:
        return self
    return self

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))