from screens.screen import Screen
import pygame, util

class AlertScreen(Screen):
  def __init__(self, data, message):
    self.data = data
    self.next = self
    self.idle = False
    self.message = message
    print("Alert created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    font = pygame.font.Font('font/font.ttf', 15)
    screen.fill(background)
    self.render_multiline(self.message, 50, 50, screen)
    space = font.render('Press SPACE to continue.', True, WHITE)
    screen.blit(space, (75, 475))

  def process_input(self, key):
    if util.is_letter(key):
      if str(chr(key)) == " ":
        self.next = None
        self.idle = True

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))