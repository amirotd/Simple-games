import random


class Game2048:
    def __init__(self):
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.init_val = [2, 4]
        self.DIMENSION = 4
        self.game_over = False

    def print_board(self):
        largest = 0
        for row in range(self.DIMENSION):
            for num in range(self.DIMENSION):
                if self.board[row][num] > largest:
                    largest = self.board[row][num]
        count = len(str(largest))

        print("=" * 20)
        for i in range(self.DIMENSION):
            print('|', end='')
            for j in range(self.DIMENSION):
                if self.board[i][j] == 0:
                    print(' ' * count + '|', end='')
                else:
                    print(' ' * (count-len(str(self.board[i][j])))+str(self.board[i][j])+'|', end='')
            print()
        print("=" * 20)


if __name__ == '__main__':
    game = Game2048()
    game.print_board()

