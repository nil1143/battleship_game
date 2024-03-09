import random


class GameBoard:
    """
    Game board object
    """

    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        """
        Convert letters to the numbers
        """
        letters_to_numbers = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
        }
        return letters_to_numbers

    def print_board(self):
        """
        Print the board
        """
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """
    Battleship object
    """

    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Function which randonly putting a ships on board coordinates
        """
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        """
        User inputs
        """
        try:
            x_row = input("Enter the row of the ship (1-8):\n")
            while x_row not in "12345678" or len(x_row) == 0:
                print("Please select a valid row")
                x_row = input("Enter the row of the ship (1-8):\n")

            y_column = input("Enter the column of the ship (A-H):\n").upper()
            while y_column not in "ABCDEFGH" or len(y_column) == 0:
                print("Please select a valid column")
                y_column = input("Enter a column of the ship (A-H):\n").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    def count_hit_ships(self):
        """
        Counting hitted ships
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def RunGame():
    """
    Geting user and computer board and creating ships
    """
    print("Welcome to the Battleship Game!\n")
    print("You have 10 attempts to guess the location of all 5 ships.")
    print("Each ship occupies a single cell on the board.")
    print("If your guess hits a ship, it will be marked as 'X' on the board.")
    print("If your guess misses, it will be marked as '-' on the board\n")
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)

    """
  Game has a 10 turns
  """
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)

        """
    Get user input
    """
        user_x_row, user_y_column = Battleship.get_user_input(object)
        """
    Check if guess duplicated
    """
        while (
            user_guess_board.board[user_x_row][user_y_column] == "-"
            or user_guess_board.board[user_x_row][user_y_column] == "X"
        ):
            print("You guessed that one already")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        """
    Check for hit or miss
    """
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk a battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        """
    Check for win or lose
    """
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit all 5 battleships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("Sorry you ran out of turns")
                GameBoard.print_board(user_guess_board)
                break


if __name__ == "__main__":
    RunGame()