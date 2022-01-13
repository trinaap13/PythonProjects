import pygame
from pygame.locals import *
import sys


class SnakeGame:

    def __init__(self):
        # Initializing pygame
        pygame.init()
        # Screen settings and size
        self.screen = pygame.display.set_mode((1000, 500))
        # Screen color
        self.screen.fill((3, 252, 140))
        self.block_x = 10
        self.block_y = 10

    def draw_block(self):
        # Screen color
        self.screen.fill((3, 252, 140))
        # Adding a block to the screen

        # Adding the block to the screen in a given x,y location
        self.screen.blit(block, (self.block_x, self.block_y))

    # Function for running the game
    def run_game(self):
        # While running the game is true:
        while True:
            # When something happens in the game...
            for event in pygame.event.get():
                # If that thing happening is a KEYDOWN
                if event.type == KEYDOWN:
                    # Quit if esc is pressed
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_UP:
                        self.block_y -= 10
                        self.draw_block()
                    if event.key == K_DOWN:
                        self.block_y += 10
                        self.draw_block()
                    if event.key == K_LEFT:
                        self.block_x -= 10
                        self.draw_block()
                    if event.key == K_RIGHT:
                        self.block_x += 10
                        self.draw_block()
                elif event.type == pygame.QUIT:
                    sys.exit()
            # Apply any changes made
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    block = pygame.image.load("SnakeGame/resources/snake skin.jpeg")
    ai = SnakeGame()
    ai.run_game()
