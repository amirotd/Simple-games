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
        """
         This method prints the whole game main board in tables
        """
        largest = 0
        for row in range(self.DIMENSION):   # finds the largest number in the board
            for num in range(self.DIMENSION):
                if self.board[row][num] > largest:
                    largest = self.board[row][num]
        count = len(str(largest))   # every cell of the table will be equal to the size of the largest number

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

    def generate_random(self):
        """
         This method generates two random numbers,
        this two numbers are the coordinate of a cell
        """
        ran_x = random.randrange(0, self.DIMENSION, 1)
        ran_y = random.randrange(0, self.DIMENSION, 1)
        if self.board[ran_x][ran_y] != 0:   # return numbers if the cell is empty
            return self.generate_random()
        else:
            return ran_x, ran_y

    def main(self):
        """
        This method is the main loop of the game
        """
        while not self.game_over:
            valid_input = True
            direction = input("Enter a direction(w,a,s,d) ").lower()

            # copy the board in another list to check if the direction made is available or not
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
