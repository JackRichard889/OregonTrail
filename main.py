import pygame

WIDTH, HEIGHT = 500, 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

def main():
  running = True
  while running:
    for event in pygame.event.get():
      if event == pygame.QUIT:
        running = False

if __name__ == "__main__":
  main()

# testing from VSCode
# new one