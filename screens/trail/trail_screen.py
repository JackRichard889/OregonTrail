from screens.screen import Screen
import pygame

class TrailScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    print("Trail screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    font = pygame.font.Font('font/font.ttf', 15)
    screen.fill(background)

  def process_input(self, key):
    print(key)