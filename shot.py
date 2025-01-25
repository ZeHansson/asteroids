import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, rotation ):
        super().__init__(x,y,SHOT_RADIUS)
        self.rotation = rotation 
    
    def draw(self, screen):
        pygame.draw.circle(screen, "blue",self.position,self.radius, 2 )

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    def update(self, dt):
        self.move(dt)