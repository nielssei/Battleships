def print_board(board):
    print("\n   0 1 2 3 4 5 6 7 8 9")
    row_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(10):
        line = row_index[i] + " |"
        for j in range(10):
            line += str(board[i][j])
            line += "|"
        print(line)

class Ship:

    def __init__(self, number, health, sunk):
        self.number = number
        self.health = health
        self.sunk = sunk

    def place_ship(self, board):

        letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f' :5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
        health_to_type= {4: 'Titanic', 3: 'Cruiser', 2: 'Yacht', 1: 'Boat'}

        overlap = True
        index = True

        while overlap == True or index == True:

            print_board(board)
            ship_start = input("Choose starting point of your " + health_to_type[self.health] + " " + self.number + "(e.g.:A4): ")

            ship_row = int(letter_to_number[ship_start[0]])
            ship_col = int(ship_start[1])

            direction_to_number = {'n': 0, 'e': 1, 's': 2, 'w': 3, 'N': 0, 'E': 1, 'S': 2, 'W': 3}
            if self.health > 1:
                ship_direction = int(direction_to_number[input("Choose a Direction for your Ship. (N: North, E: East, S: South, W: West): ")])
            else:
                ship_direction = 3

            for k in range(0, self.health):
                if ship_direction == 0:
                    if 0 <= ship_row - k < 10 and 0 <= ship_col < 10:
                        if board[ship_row - k][ship_col] == 0:
                            board[ship_row - k][ship_col] = self.number
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            for j in range(0, k):
                                board[ship_row - j][ship_col] = 0
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        for y in range(0, self.health):
                            if 0 <= ship_row - y < 10 and 0 <= ship_col < 10:
                                board[ship_row - y][ship_col] = 0

                elif ship_direction == 1:
                    if 0 <= ship_row < 10 and 0 <= (ship_col + k) < 10:
                        if board[ship_row][ship_col + k] == 0:
                            board[ship_row][ship_col + k] = self.number
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            for j in range (0, k):
                                board[ship_row][ship_col + j] = 0
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        for y in range(0, self.health):
                            if 0 <= ship_row < 10 and 0 <= ship_col + y < 10:
                                board[ship_row][ship_col + y] = 0

                elif ship_direction == 2:
                    if 0 <= ship_row + k < 10 and 0 <= ship_col < 10:
                        if board[ship_row + k][ship_col] == 0:
                            board[ship_row + k][ship_col] = self.number
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            for j in range (0, k):
                                board[ship_row + j][ship_col] = 0
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        for y in range(0, self.health):
                            if 0 <= ship_row + y < 10 and 0 <= ship_col < 10:
                                board[ship_row + y][ship_col] = 0


                elif ship_direction == 3:
                    if 0 <= ship_row < 10 and 0 <= (ship_col - k) < 10:
                        if board[ship_row][ship_col - k] == 0:
                            board[ship_row][ship_col - k] = self.number
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            for j in range (0, k):
                                board[ship_row][ship_col - j] = 0
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        for y in range(0, self.health):
                            if 0 <= ship_row < 10 and 0 <= ship_col - y < 10:
                                board[ship_row][ship_col - y] = 0

                else:
                    print("invalid")
