import random
import copy


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

    def main(self):
        while not self.game_over:
            valid_input = True
            direction = input("Enter a direction(w,a,s,d) ").lower()
            temp_board = copy.deepcopy(self.board)

            if direction == 'w':
                pass
            elif direction == 'a':
                pass
            elif direction == 's':
                pass
            elif direction == 'd':
                pass
            elif direction == 'exit':
                break
            else:
                valid_input = False

            if not valid_input:
                print("please enter a valid direction!")
            else:
                if self.board == temp_board:
                    print("try diff direction")


if __name__ == '__main__':
    game = Game2048()
    game.print_board()
    game.main()
