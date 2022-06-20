from battleship_setup import *

letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
row_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
tries = 0

guess_board = [['0'] * 10 for x in range(10)]
created_board = [['0'] * 10 for y in range(10)]

print("Place your Ships. You have 4 different types of ships:"
      "\n"
      "\n- Titanic. 4 units long. 1 available."
      "\n- Cruiser. 3 units long. 2 available."
      "\n- Yacht. 2 units long. 3 available"
      "\n- Boat. 1 unit long. 4 available. \n")

titanic_1 = Ship("Titanic", "1", 4)
cruiser_1 = Ship("Cruiser", "1", 3)
cruiser_2 = Ship("Cruiser", "2", 3)
yacht_1 = Ship("Yacht", "1", 2)
yacht_2 = Ship("Yacht", "2", 2)
yacht_3 = Ship("Yacht", "3", 2)
boat_1 = Ship("Boat", "1", 1)
boat_2 = Ship("Boat", "2", 1)
boat_3 = Ship("Boat", "3", 1)
boat_4 = Ship("Boat", "4", 1)

titanic_1.place_ship(created_board)
cruiser_1.place_ship(created_board)
cruiser_2.place_ship(created_board)
yacht_1.place_ship(created_board)
yacht_2.place_ship(created_board)
yacht_3.place_ship(created_board)
boat_1.place_ship(created_board)
boat_2.place_ship(created_board)
boat_3.place_ship(created_board)
boat_4.place_ship(created_board)

print_board(created_board)

print("This is your final board.")
print("\nLet's start guessing your Opponents ships. You have 10 tries.")
while tries < 10:
    print_board(guess_board)

    locationInput = input("Enter a Location (e.g. A3): ")

    rowInput = int(letter_to_number[locationInput[0]])
    colInput = int(locationInput[1])

    if 0 < colInput < 10 and 0 < rowInput < 10:
        if created_board[rowInput][colInput] == 'X':
            guess_board[rowInput][colInput] = 'X'
            tries += 1
            print('\nYou hit a ship! ' + str(10 - tries) + ' tries left\n')

        else:
            guess_board[rowInput][colInput] = '-'
            tries += 1
            print('\nNo ships hit... ' + str(10 - tries) + ' tries left\n')
    else:
        print('\nNUMBER(S) OUT OF RANGE. PLEASE TYPE A NUMBER BETWEEN 0 and 7\n')

