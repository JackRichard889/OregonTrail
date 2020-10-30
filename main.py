import pygame
from date import Date

WIDTH, HEIGHT = 500, 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, BLUE)
screen.blit(img, (20, 20))

pygame.display.update()
def main():
  running = True
  while running:
    for event in pygame.event.get():
      if event == pygame.QUIT:
        running = False
    clock.tick(60)

if __name__ == "__main__":
  main()

# testing from VSCode
# new one