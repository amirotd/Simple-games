import sys
import pygame
from Engine import Game2048
import copy


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
                                                        (self.SQ_SIZE, self.SQ_SIZE))

    def refresh(self, surface, stat):
        self.load_board(surface)
        self.update_blocks(surface, stat)

    def load_board(self, surface):
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                pygame.draw.rect(surface, 'grey', [col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE])
                pygame.draw.rect(surface, 'dark grey', [col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE], 1)

    def update_blocks(self, surface, stat):
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                block = stat.board[row][col]
                if block != 0:
                    surface.blit(self.IMAGES[str(block)],
                                 [col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE])

    def main(self):
        self.load_images()
        status = Game2048()
        pygame.display.set_caption("2048 Game")
        pygame.display.set_icon(self.IMAGES['2048'])
        main_board = pygame.display.set_mode(self.SCREEN_COORDINATES)
        main_board.fill(pygame.Color("grey"))

        status.get_random_num()
        status.get_random_num()

        while True:
            temp_board = copy.deepcopy(status.board)

            # Events loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        status.slide_up(status.board)

                    if event.key == pygame.K_s:
                        status.slide_down(status.board)

                    if event.key == pygame.K_a:
                        status.slide_left(status.board)

                    if event.key == pygame.K_d:
                        status.slide_right(status.board)

                    if status.board == temp_board:
                        print("try diff direction")
                    else:
                        if status.check_winning():
                            print("***you won!***")
                            break
                        else:
                            status.get_random_num()

                            if status.check_losing():
                                print("you lost :(")
                                break
            self.refresh(main_board, status)
            pygame.display.update()


if __name__ == '__main__':
    x = GameGUI()
    x.main()
