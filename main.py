import pygame
from screens.main_screen import MainScreen

WIDTH, HEIGHT = 500, 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

def main():
  screens = [MainScreen()]
  while len(screens) > 0:
    screens[-1].render(screen)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        screens.clear()
        break
      elif event.type == pygame.KEYDOWN:
        newScreen = screens[-1].process_input(event.key)
        if newScreen == None:
          screens.pop()
        elif newScreen.__class__ != screens[-1].__class__:
          screens.append(newScreen)

main()