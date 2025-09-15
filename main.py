import pygame
from constants import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    new_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print(
        "Starting Asteroids!"
        "\nScreen width: 1280"
        "\nScreen height: 720"
        )
    
    while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
      screen.fill((0, 0, 0))
      player.draw(screen)
      player.update(dt)
      pygame.display.flip()
      dt = new_clock.tick(60) / 1000

if __name__ == "__main__":
    main()