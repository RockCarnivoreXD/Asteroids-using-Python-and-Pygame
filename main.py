import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print(
        "Starting Asteroids!"
        "\nScreen width: 1280"
        "\nScreen height: 720"
        )


if __name__ == "__main__":
    main()