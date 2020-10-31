import pygame
from screens.main_screen import MainScreen

WIDTH, HEIGHT = 500, 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

def main():
  currentScreen = MainScreen()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN:
        currentScreen = currentScreen.process_input(event.key)
        if currentScreen == None:
          currentScreen = MainScreen()
    currentScreen.render(screen)
    pygame.display.update()
    clock.tick(60)

main()