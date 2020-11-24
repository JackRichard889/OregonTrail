from screens.screen import Screen
import pygame
import util
from environment import Landmarks


class SplashScreen(Screen):
  def __init__(self, data, landmark, result):
    self.data = data
    self.next = self
    self.idle = False
    self.result = result
    self.landmark = landmark;
    print("Splash screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    
    font = pygame.font.Font('font/font.ttf', 20)
    screen.blit(Landmarks.assets[self.landmark], (0, 0))
    pygame.draw.rect(screen, background, pygame.Rect(0, 400, 500, 500))

    location = font.render(Landmarks.names[self.landmark], True, WHITE)
    space = font.render('Press SPACE to continue.', True, WHITE)
    dateText = font.render(self.data["date"].get_formatted_date(), True, WHITE)

    screen.blit(location, location.get_rect(center=(500//2, 425)))
    screen.blit(dateText, dateText.get_rect(center=(500//2, 450)))
    screen.blit(space, space.get_rect(center=(500//2, 480)))

  def process_input(self, key):
    if util.is_letter(key):
      if str(chr(key)) == " ":
        self.next = self.result
        self.idle = True