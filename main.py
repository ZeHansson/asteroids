# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    fps_limiter = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    while True:
        #Kill switch
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #1

        #2

        #3 Draw!
        screen.fill("black")
        
        pygame.display.flip()
        dt = fps_limiter.tick(60)/1000
        


if __name__ == "__main__":
    main()