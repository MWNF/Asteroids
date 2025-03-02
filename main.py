import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
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
        updateable.update(dt)
        #refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()