import sys
import pygame
from Engine import Game2048
import copy


class GameGUI:
    def __init__(self):
        self.SCREEN_COORDINATES = (500, 600)
        self.BOARD_COORDINATES = (self.SCREEN_COORDINATES[0]-100, self.SCREEN_COORDINATES[1]-200)
        self.DIMENSION = 4
        self.SQ_SIZE = self.BOARD_COORDINATES[0] // self.DIMENSION
        self.SQ_BORDER = 3
        self.IMAGES = {}

        pygame.init()
        self.font = pygame.font.SysFont('arial', 40)

    def load_images(self):
        """
         This method loads images into pygame.
        """
        blocks = ['2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048']
        for block in blocks:
            image_size = (self.SQ_SIZE-(self.SQ_BORDER*2), self.SQ_SIZE-(self.SQ_BORDER*2))
            self.IMAGES[block] = pygame.transform.scale(pygame.image.load("images/" + block + ".png"), image_size)

    def refresh(self, screen, surface, stat):
        pygame.draw.rect(screen, 'dark grey', [0, 0, self.SCREEN_COORDINATES[0], self.SCREEN_COORDINATES[1]])
        screen.blit(surface, [50, 150, self.BOARD_COORDINATES[0], self.BOARD_COORDINATES[1]])

        if stat.check_losing():
            self.losing_message(screen)
        else:
            self.load_board(surface)
        self.update_blocks(surface, stat)
        self.update_score(screen, stat)

    def load_board(self, surface):
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                rect = [col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE]
                pygame.draw.rect(surface, 'grey', rect)
                pygame.draw.rect(surface, 'dark grey', rect, self.SQ_BORDER)

    def update_blocks(self, surface, stat):
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                block = stat.board[row][col]
                if block != 0:
                    rect = [col * self.SQ_SIZE + self.SQ_BORDER, row * self.SQ_SIZE + self.SQ_BORDER, self.SQ_SIZE, self.SQ_SIZE]
                    surface.blit(self.IMAGES[str(block)], rect)

    def update_score(self, screen, stat):
        score_surface = self.font.render("Score: " + str(stat.score), True, "0x494949")
        score_rect = score_surface.get_rect(topleft=(50, 80))
        screen.blit(score_surface, score_rect)

    def losing_message(self, screen):
        losing_surface = pygame.Surface((self.BOARD_COORDINATES[0], self.BOARD_COORDINATES[1]))
        losing_surface.set_alpha(100)
        losing_surface.fill("red")

        losing_text = self.font.render("You Lost!", True, "white")
        losing_text_rect = losing_text.get_rect(center=(self.BOARD_COORDINATES[0] // 2, self.BOARD_COORDINATES[1] // 2))
        losing_surface.blit(losing_text, losing_text_rect)
        screen.blit(losing_surface, (50, 150))

    def main(self):
        self.load_images()
        status = Game2048()
        pygame.display.set_caption("2048 Game")
        pygame.display.set_icon(self.IMAGES['2048'])

        screen = pygame.display.set_mode(self.SCREEN_COORDINATES)
        screen.fill(pygame.Color("dark grey"))

        main_board = pygame.Surface(self.BOARD_COORDINATES)
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
            self.refresh(screen, main_board, status)
            pygame.display.update()


if __name__ == '__main__':
    x = GameGUI()
    x.main()
