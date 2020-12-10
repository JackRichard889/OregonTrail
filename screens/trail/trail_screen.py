from screens.screen import Screen
import pygame
from environment import Ground
from skybox import *

class TrailScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    print("Trail screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    font = pygame.font.Font('font/font.ttf', 15)
    i = 500
    render_skybox(screen, self.data["date"].get_date().time())
    screen.blit(Ground.render(self.data["environments"]), (-self.data["trailLength"] + i, 0))

  def process_input(self, key):
    print(key)