import pygame
import sys

from paddle import Paddle


class PingPong:
    def __init__(self):
        # This is to initialize the game.
        pygame.init()

        self.width = 1000
        self.height = 600

        # Creating screen and captions
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Ping Pong')

        # Initialize paddle
        self.paddle = Paddle(self)

    def run_game(self):
        # Loop each event (screen).
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Display and draw.
            self.paddle.draw_paddle()
            pygame.display.flip()


if __name__ == '__main__':
    my_game = PingPong()
    my_game.run_game()
