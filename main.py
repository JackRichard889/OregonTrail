import pygame
from screens.main_screen import MainScreen
from date import Date
from environment import EnvironmentRegistry

WIDTH, HEIGHT = 500, 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

def main():
  registry = EnvironmentRegistry()
  data = {"date": Date(4, 0), "pace": 0, "rations": 0, "environments": registry.get_array(), "trailLength": registry.get_length()}
  screens = [MainScreen(data)]

  while len(screens) > 0:
    screens[-1].receive_data(data)
    screens[-1].render(screen)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        screens.clear()
        break
      elif event.type == pygame.KEYDOWN:
        screens[-1].process_input(event.key)
        newScreen = screens[-1].listen_for_transition()
        if newScreen == None:
          screens.pop()
          if len(screens) < 1:
            return
        elif newScreen.__class__ != screens[-1].__class__:
          screens.append(newScreen)
    for scr in screens:
      if scr.idle:
        screens.remove(scr)
    data = screens[-1].sync_data()

main()