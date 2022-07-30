import os
import sys
import select
import tty
import termios
import random
import time
from copy import deepcopy


class Tetris:
    def __init__(self):
        self.O = [[1, 1],
                  [1, 1]]

        self.I = [[1], [1], [1], [1]]

        self.Z = [[1, 1, 0],
                  [0, 1, 1]]

        self.S = [[0, 1, 1],
                  [1, 1, 0]]

        self.T = [[0, 1, 0],
                  [1, 1, 1]]

        self.L = [[1, 0],
                  [1, 0],
                  [1, 1]]

        self.J = [[0, 1],
                  [0, 1],
                  [1, 1]]

        self.pieces = [self.S, self.Z, self.I, self.O, self.J, self.L, self.T]
        self.board = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                      [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]

    @staticmethod
    def clear_screen():
        os.system('clear')

    def print_board(self, current_piece, piece_pos):
        self.clear_screen()
        board_copy = deepcopy(self.board)
        current_piece_size_y = len(current_piece)
        current_piece_size_x = len(current_piece[0])
        for i in range(current_piece_size_y):
            for j in range(current_piece_size_x):
                board_copy[piece_pos[0]+i][piece_pos[1]+j] = current_piece[i][j] | self.board[piece_pos[0]+i][piece_pos[1]+j]

        print("")
        print(" " * 10 + "\033[1;32m =" * 12)
        for i in range(22):
            print(" " * 10, end='')
            for j in range(12):
                if board_copy[i][j] == 1:
                    print("▌▌", end='')
                elif board_copy[i][j] == 2:
                    print("|+|", end='')
                elif board_copy[i][j] == 3:
                    print(" =", end='')
                else:
                    print("..", end='')

            print("")

    def get_piece(self):
        return random.choice(self.pieces)

    @staticmethod
    def get_down(piece_pos):
        new_piece_pos = [piece_pos[0] + 1, piece_pos[1]]
        return new_piece_pos

    @staticmethod
    def get_left(piece_pos):
        new_piece_pos = [piece_pos[0], piece_pos[1] - 1]
        return new_piece_pos

    @staticmethod
    def get_right(piece_pos):
        new_piece_pos = [piece_pos[0], piece_pos[1] + 1]
        return new_piece_pos

    @staticmethod
    def rotate_piece(piece):
        piece_copy = deepcopy(piece)
        reverse_piece = piece_copy[::-1]
        return list(list(elem) for elem in zip(*reverse_piece))

    @staticmethod
    def kbhit():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def main(self):
        current_piece = self.get_piece()
        piece_pos = [0, 4]
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            self.clear_screen()
            input('press ENTER to start...')
            while True:
                if self.kbhit():
                    c = sys.stdin.read(1)
                    if c == 'w':
                        current_piece = self.rotate_piece(current_piece)
                    if c == 'a':
                        piece_pos = self.get_left(piece_pos)
                    if c == 'd':
                        piece_pos = self.get_right(piece_pos)
                    if c == 's':
                        piece_pos = self.get_down(piece_pos)
                    if c == 'g':
                        break

                piece_pos = self.get_down(piece_pos)
                self.print_board(current_piece, piece_pos)
                time.sleep(0.3)

        finally:
            self.clear_screen()
            print("game over")
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


if __name__ == '__main__':
    print("Hello this is Tetris")
    tetris = Tetris()
    tetris.main()
