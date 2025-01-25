import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        #self.x = x
        #self.y = y
        #self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else: 
            angle_1 = random.uniform(20.00,50.00)
            baby_1_direction = self.velocity.rotate(angle_1)
            baby_2_direction = self.velocity.rotate(-angle_1)
            baby_1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            baby_1.velocity = baby_1_direction*1.2
            baby_2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            baby_2.velocity = baby_2_direction*1.2




