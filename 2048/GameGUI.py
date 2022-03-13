import sys
import pygame
from Engine import Game2048


class GameGUI:
    def __init__(self):
        self.SCREEN_COORDINATES = (512, 512)
        self.DIMENSION = 4
        self.SQ_SIZE = self.SCREEN_COORDINATES[0] // self.DIMENSION
        self.IMAGES = {}

        pygame.init()

    def load_images(self):
        """
         This method loads images into pygame.
        """
        blocks = ['2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048']
        for block in blocks:
            self.IMAGES[block] = pygame.transform.scale(pygame.image.load("images/" + block + ".svg"),
                                                        (self.SQ_SIZE, self.SQ_SIZE))

    def main(self):
        self.load_images()

        while True:
            pygame.display.set_caption("2048 Game")
            main_board = pygame.display.set_mode(self.SCREEN_COORDINATES)
            main_board.fill(pygame.Color("black"))

            # Events loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':
    x = GameGUI()
    x.main()
