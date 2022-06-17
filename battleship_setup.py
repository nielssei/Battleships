class Board:

    def __init__(self, board):
        self.board = board

    def print_board(self):
        print("\n   0 1 2 3 4 5 6 7 ")
        row_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(8):
            line = row_index[i] + " |"
            for j in range(8):
                line += self.board[i][j]
                line += "|"
            print(line)

    def create_empty_board(self, board):
        self.board = [[], [], [], [], [], [], [], []]
        for i in range(8):
            self.board[i].append('0')
            for j in range(8):
                self.board[j].append('0')

    def check_if_onboard(self):
        pass

    def check_if_overlap(self):
        pass

class Ship:

    def __init__(self, type, number):
        self.type = type
        self.number = number

    def place_ship(self, created_board):

        length = 0
        if self.type == "Titanic":
            length = 4
        elif self.type == "Cruiser":
            length = 3
        elif self.type == "Yacht":
            length = 2
        elif self.type == "Boat":
            length = 1

        letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        ship_start = input("Choose starting point of your " + self.type + " " + self.number + "(Example: A4): ")

        ship_row = int(letter_to_number[ship_start[0]])
        ship_col = int(ship_start[1])

        if length > 1:
            ship_direction = int(input("Choose a Direction for your Ship. (0: North, 1: East, 2: South, 3: West): "))
        else:
            ship_direction = 0

        for k in range(0, length):
            if ship_direction == 0:
                created_board[ship_row - k][ship_col] = 'X'
            elif ship_direction == 1:
                created_board[ship_row][ship_col + k] = 'X'
            elif ship_direction == 2:
                created_board[ship_row + k][ship_col] = 'X'
            elif ship_direction == 3:
                created_board[ship_row][ship_col - k] = 'X'
