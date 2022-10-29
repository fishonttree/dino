import pygame

class Paddle:
    """A class to simulate paddle."""
    def __init__(self, pg):
        # Inheriting from class PingPong.
        # For more from inheritance, google 'Class Inheritance'.
        super().__init__()

        # Initialize screen
        self.screen = pg.screen
        self.screen_rect = self.screen.get_rect()

        # Create paddle image
        self.paddle_img = pygame.image.load('images/paddle.bmp')

        # Convert paddle image to smaller size
        self.small_img = pygame.transform.scale(self.paddle_img, (75, 200))

        # Create paddle rectangle.
        self.paddle_rect = self.paddle_img.get_rect()


    def draw_paddle(self):
        # Draw paddle.
        self.screen.blit(self.small_img, self.paddle_rect)


    #def move_paddle(self):
