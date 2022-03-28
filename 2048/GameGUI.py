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

        self.end_screen_value = 0
        self.menu_screen_value = 0
        self.menu_on = False

        pygame.init()
        self.font = pygame.font.SysFont('arial', 35)
        self.font2 = pygame.font.SysFont('arial black', 60)

        self.clock = pygame.time.Clock()

    def load_images(self):
        """
         This method loads images into pygame.
        """
        blocks = ['2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048']
        self.IMAGES['menu'] = pygame.transform.scale(pygame.image.load("images/menu.png"), [self.SQ_SIZE, self.SQ_SIZE-20])
        self.IMAGES['undo'] = pygame.transform.scale(pygame.image.load("images/undo.png"), [self.SQ_SIZE//2, self.SQ_SIZE//2])
        for block in blocks:
            image_size = (self.SQ_SIZE-(self.SQ_BORDER*2), self.SQ_SIZE-(self.SQ_BORDER*2))
            self.IMAGES[block] = pygame.transform.scale(pygame.image.load("images/" + block + ".png"), image_size)

    def refresh(self, screen, surface, stat):
        pygame.draw.rect(screen, 'dark grey', [0, 0, self.SCREEN_COORDINATES[0], self.SCREEN_COORDINATES[1]])
        screen.blit(surface, [50, 150, self.BOARD_COORDINATES[0], self.BOARD_COORDINATES[1]])
        screen.blit(self.IMAGES['undo'], [(7*self.SQ_SIZE//2)+50-self.SQ_BORDER, 150-self.SQ_SIZE//2])

        if stat.check_losing():
            self.ending_message(screen, "You Lost!", "red")
        elif stat.check_winning():
            self.ending_message(screen, "You Won!", "green")
        self.load_board(surface)
        self.update_blocks(surface, stat)
        self.update_score(screen, stat)
        if self.menu_on:
            self.menu(screen)
        screen.blit(self.IMAGES['menu'], [self.SCREEN_COORDINATES[0] - self.SQ_SIZE, 0, self.SQ_SIZE, self.SQ_SIZE-20])

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
        score_text = "High Score: " + str(0) + "\n" + "Score: " + str(stat.score)  # Todo: add highScore in Engine.py
        lines = score_text.splitlines()
        for i, line in enumerate(lines):
            text = self.font.render(line, True, "0x494949")
            rect = text.get_rect(topleft=(60, 50 + i*50))
            screen.blit(text, rect)
        # score_surface = self.font.render("Score: " + str(stat.score), True, "0x494949")
        # score_rect = score_surface.get_rect(topleft=(50, 80))
        # screen.blit(score_surface, score_rect)

    def ending_message(self, screen, message: str, color: str):
        if self.end_screen_value != self.BOARD_COORDINATES[0]:
            self.end_screen_value += 10
        ending_surface = pygame.Surface((self.end_screen_value, self.end_screen_value))
        ending_surface.set_alpha(100)
        ending_surface.fill(color)

        ending_text = self.font2.render(message, True, "white")
        ending_text_rect = ending_text.get_rect(center=(self.SCREEN_COORDINATES[0]//2, self.SCREEN_COORDINATES[1]//2))

        try_again_text = "Do you want to play again?\nYes[Y]   No[N]"   # Todo: make Yes and No work
        lines = try_again_text.splitlines()

        screen.blit(ending_surface, (self.SQ_SIZE * 2 + 50 - self.end_screen_value // 2, self.SQ_SIZE * 2 + 150 - self.end_screen_value // 2))
        screen.blit(ending_text, ending_text_rect)
        for i, line in enumerate(lines):
            text = self.font.render(line, True, "white")
            rect = text.get_rect(center=(self.SCREEN_COORDINATES[0] // 2, self.SCREEN_COORDINATES[1] // 2 + 70 + i*50))
            screen.blit(text, rect)

    def menu(self, screen):  # Todo: make every item in menu work
        if self.menu_screen_value != self.SCREEN_COORDINATES[0]:
            self.menu_screen_value += 20
        menu_surface = pygame.Surface((self.menu_screen_value, self.menu_screen_value+100))
        menu_surface.set_alpha(150)
        menu_surface.fill("blue")

        menu_text = "Rest Game\nUndo\nAbout\nExit"
        lines = menu_text.splitlines()

        screen.blit(menu_surface, (self.SQ_SIZE * 2 + 50 - self.menu_screen_value // 2, self.SQ_SIZE * 2 + 50 - self.menu_screen_value // 2))
        for i, line in enumerate(lines):
            text = self.font2.render(line, True, "white")
            rect = text.get_rect(center=(self.SCREEN_COORDINATES[0]//2, self.SCREEN_COORDINATES[1]//2 - 150 + i*100))
            screen.blit(text, rect)

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location = pygame.mouse.get_pos()
                    xu1 = self.SCREEN_COORDINATES[0]-(self.SQ_SIZE//2)-50
                    xu2 = self.SCREEN_COORDINATES[0]-50
                    yu1 = 150-self.SQ_SIZE//2
                    yu2 = 150

                    if xu1 < location[0] < xu2 and yu1 < location[1] < yu2:
                        status.undo()

                    x1 = self.SCREEN_COORDINATES[0]-self.SQ_SIZE
                    x2 = self.SCREEN_COORDINATES[0]
                    y2 = self.SQ_SIZE-20

                    if x1 < location[0] < x2 and 0 < location[1] < y2:
                        if self.menu_on:
                            self.menu_on = False
                            self.menu_screen_value = 0
                        else:
                            self.menu_on = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        status.undo()
                    if not status.check_winning() and not status.check_losing() and not self.menu_on:
                        if event.key == pygame.K_w:
                            status.save_last_values()
                            status.slide_up(status.board)

                        if event.key == pygame.K_s:
                            status.save_last_values()
                            status.slide_down(status.board)

                        if event.key == pygame.K_a:
                            status.save_last_values()
                            status.slide_left(status.board)

                        if event.key == pygame.K_d:
                            status.save_last_values()
                            status.slide_right(status.board)

                        if event.key == pygame.K_r:
                            status.reset_game()

                        if status.board == temp_board:
                            print("try diff direction")
                        else:
                            if status.board != status.last_move:
                                status.get_random_num()

                    # if status.board == temp_board:
                    #     print("try diff direction")
                    # else:
                    #     if status.check_winning():
                    #         print("***you won!***")
                    #         break
                    #     else:
                    #         status.get_random_num()
                    #
                    #         if status.check_losing():
                    #             print("you lost :(")
                    #             break
            self.refresh(screen, main_board, status)
            pygame.display.update()
            self.clock.tick(120)


if __name__ == '__main__':
    game = GameGUI()
    game.main()
