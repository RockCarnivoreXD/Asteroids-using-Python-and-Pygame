import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    new_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

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
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid) == True:
                print("Game over!")
                sys.exit()
                
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    shot.kill()
                    asteroid.kill()
                    break
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = new_clock.tick(60) / 1000

if __name__ == "__main__":
    main()