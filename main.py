import pygame
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # This checks to see if the user closed the window and exit the game if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the screen black
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        #refresh the screen
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()