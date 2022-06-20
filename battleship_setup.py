def print_board(board):
    print("\n   0 1 2 3 4 5 6 7 8 9")
    row_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(10):
        line = row_index[i] + " |"
        for j in range(10):
            line += board[i][j]
            line += "|"
        print(line)


class Ship:

    def __init__(self, ship_type, number, health):
        self.ship_type = ship_type
        self.number = number
        self.health = health

    def place_ship(self, board):

        length = 0
        if self.ship_type == "Titanic":
            length = 4
        elif self.ship_type == "Cruiser":
            length = 3
        elif self.ship_type == "Yacht":
            length = 2
        elif self.ship_type == "Boat":
            length = 1

        letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

        overlap = True
        index = True

        while overlap == True or index == True:

            ship_start = input("Choose starting point of your " + self.ship_type + " " + self.number + "(E.G.:A4): ")

            ship_row = int(letter_to_number[ship_start[0]])
            ship_col = int(ship_start[1])

            if length > 1:
                ship_direction = int(input("Choose a Direction for your Ship. (0: North, 1: East, 2: South, 3: West): "))
            else:
                ship_direction = 3

            for k in range(0, length):
                if ship_direction == 0:
                    if 0 <= ship_row - k < 10 and 0 <= ship_col < 10:
                        if board[ship_row - k][ship_col] != 'X':
                            board[ship_row - k][ship_col] = 'X'
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        break
                elif ship_direction == 1:
                    if 0 <= ship_row < 10 and 0 <= (ship_col + k) < 10:
                        if board[ship_row][ship_col + k] != 'X':
                            board[ship_row][ship_col + k] = 'X'
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        break
                elif ship_direction == 2:
                    if 0 <= ship_row + k < 10 and 0 <= ship_col < 10:
                        if board[ship_row + k][ship_col] != 'X':
                            board[ship_row + k][ship_col] = 'X'
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        break

                elif ship_direction == 3:
                    if 0 <= ship_row < 10 and 0 <= (ship_col - k) < 10:
                        if board[ship_row][ship_col - k] != 'X':
                            board[ship_row][ship_col - k] = 'X'
                            overlap = False
                            index = False
                        else:
                            print("Ship Overlapping! Try again.")
                            overlap = True
                            break
                    else:
                        index = True
                        print("Ship out of Map. Try again.")
                        break

                else:

                    print("invalid")
