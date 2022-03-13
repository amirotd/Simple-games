import sys
import pygame
from Engine import Game2048


class GameGUI:
    def __init__(self):
        self.SCREEN_COORDINATES = (400, 400)
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
            self.IMAGES[block] = pygame.transform.scale(pygame.image.load("images/" + block + ".png"),
                                                        (self.SQ_SIZE, self.SQ_SIZE)).convert()

    def refresh(self, surface, stat):
        self.load_board(surface)
        self.update_blocks(surface, stat)

    def load_board(self, surface):
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                pygame.draw.rect(surface, 'red', [col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE], 1)

    def update_blocks(self, surface, stat):
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                block = stat.board[row][col]
                if block != 0:
                    surface.blit(self.IMAGES[str(block)],
                                 [col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE])

    def main(self):

        status = Game2048()
        pygame.display.set_caption("2048 Game")
        main_board = pygame.display.set_mode(self.SCREEN_COORDINATES)
        main_board.fill(pygame.Color("grey"))
        self.load_images()

        while True:
            # Events loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.refresh(main_board, status)
            pygame.display.update()


if __name__ == '__main__':
    x = GameGUI()
    x.main()
