import pygame
import sys
import random
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    SCORE = 0
    PLAYER_LIVES = 3
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field_of_asteroids = AsteroidField()
    while True:
        # This checks to see if the user closed the window and exit the game if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #limits the FPS to 60 and takes the delta time return and divides to convert from ms to s
        dt = clock.tick(60) / 1000
        # fill the screen black
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        #checking for collision
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                if PLAYER_LIVES > 0:
                    PLAYER_LIVES -= 1
                    player.kill()
                    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
                else:
                    print("Game over!")
                    print(f"FINAL SCORE: {SCORE}")
                    sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
                    SCORE += 100
        #refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()