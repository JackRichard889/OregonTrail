from screens.screen import Screen
from screens.learn_screen import LearnScreen
import pygame


class MainScreen(Screen):
  def __init__(self):
    print("Main screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 29)
    title = font.render('The Oregon Trail', True, WHITE)
    self.render_multiline(
            "You may:\n\n\n  1. Travel the trail\n  2. Learn about the trail\n  3. End\n\n\nWhat is your choice? _",
            35, 120, screen)
    screen.blit(title, (24, 40))

  def process_input(self, key):
    charKey = str(chr(key))
    if charKey == "1":
      print("Travel")
    elif charKey == "2":
      return LearnScreen()
    elif charKey == "3":
      return None
    return self

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))
