# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    fps_limiter = pygame.time.Clock()
    dt = 0
    

    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

 
    


    while True:
        #Kill switch
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #1


        #2 Update!
        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()
        #3 Draw!
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        
        
        
        pygame.display.flip()
        dt = fps_limiter.tick(60)/1000
        


if __name__ == "__main__":
    main()